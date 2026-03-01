from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # list_display shows these columns in the user list table
    list_display = ('username', 'email', 'date_of_birth', 'is_staff')
    
    # fieldsets adds fields to the 'Edit User' page
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
    # add_fieldsets adds fields to the 'Add User' page
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CustomUser, CustomUserAdmin)