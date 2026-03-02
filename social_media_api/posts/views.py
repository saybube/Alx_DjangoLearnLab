from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.response import Response
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from accounts.models import CustomUser
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

# Create your views here.
class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    # Fields allowed for sorting (?ordering=...)
    ordering_fields = ['created_at', 'updated_at']
    # Default sorting (The '-' sign means descending/newest first)
    ordering = ['-created_at']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostFeedView(generics.ListAPIView):
    """
    View to retrieve a feed of posts from users that the current user follows.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 1. Get the list of users the current user is following
        # request.user.following.all() works because of the ManyToMany field we set up
        following_users = self.request.user.following.all()
        
        # 2. Filter posts where the author is in that 'following_users' list
        # 3. Order by '-created_at' to show the most recent posts first
        return Post.objects.filter(author__in=following_users).order_by('-created_at')
    
class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # 1. Use generics.get_object_or_404(Post, pk=pk) to find the post
        post = get_object_or_404(Post, pk=pk)
        
        # 2. Use get_or_create to ensure a user doesn't like a post multiple times
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if not created:
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # 3. Generate a Notification for the post author (if it's not the user themselves)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb='liked your post',
                target=post,
                target_content_type=ContentType.objects.get_for_model(Post),
                target_object_id=post.id
            )

        return Response({"message": "Post liked successfully."}, status=status.HTTP_201_CREATED)

class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        # 1. Ensure post exists
        post = get_object_or_404(Post, pk=pk)
        
        # 2. Find and delete the like
        like = Like.objects.filter(user=request.user, post=post).first()
        
        if like:
            like.delete()
            return Response({"message": "Post unliked successfully."}, status=status.HTTP_200_OK)
        
        return Response({"message": "You haven't liked this post yet."}, status=status.HTTP_400_BAD_REQUEST)