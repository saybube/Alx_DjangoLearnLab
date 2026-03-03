# Social Media API

A robust RESTful API built with Django and Django REST Framework that simulates core social media functionalities, including user authentication, content management, a dynamic follow system, and real-time-style notifications.

---

## Features

- **User Management** – Custom user models, registration, and token-based authentication.
- **Profiles** – Personalized bios and profile pictures.
- **Posts & Comments** – Full CRUD functionality with author tracking.
- **Follow System** – Follow/unfollow users to curate a personal feed.
- **Feed** – A dedicated endpoint to view posts only from users you follow.
- **Likes** – Like or unlike posts.
- **Notifications** – Get notified when someone follows you or likes your posts via a `GenericForeignKey` system.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 4.2+ |
| API | Django REST Framework |
| Database | SQLite (Development) / PostgreSQL (Production) |
| Authentication | Token Authentication |

---

## API Endpoints

### Accounts & Authentication

| Endpoint | Method | Description |
|---|---|---|
| `/api/accounts/register/` | `POST` | Create a new account and receive a token. |
| `/api/accounts/login/` | `POST` | Exchange credentials for an auth token. |
| `/api/accounts/profile/` | `GET` / `PUT` | View or update your profile details. |
| `/api/accounts/follow/<int:user_id>/` | `POST` | Follow a specific user. |
| `/api/accounts/unfollow/<int:user_id>/` | `POST` | Unfollow a specific user. |

### Posts & Social Interaction

| Endpoint | Method | Description |
|---|---|---|
| `/api/posts/` | `GET` / `POST` | List all posts or create a new one. |
| `/api/posts/<int:pk>/` | `GET` / `PUT` / `DELETE` | View, edit, or delete a specific post. |
| `/api/posts/feed/` | `GET` | Retrieve posts from followed users, newest first. |
| `/api/posts/<int:pk>/like/` | `POST` | Like a specific post. |
| `/api/posts/<int:pk>/unlike/` | `POST` | Remove a like from a post. |

### Notifications

| Endpoint | Method | Description |
|---|---|---|
| `/api/notifications/` | `GET` | List all notifications for the authenticated user. |

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/social_media_api.git
   cd social_media_api
```

2. **Set up a virtual environment**
```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
   pip install -r requirements.txt
```

4. **Apply migrations**
```bash
   python manage.py makemigrations
   python manage.py migrate
```

5. **Run the server**
```bash
   python manage.py runserver
```

---

## Testing the Logic Flow

1. Register two users — **User A** and **User B**.
2. Post something as **User B**.
3. Follow **User B** using **User A's** token.
4. Check the feed as **User A** — User B's post should now appear.
5. Like **User B's** post as **User A**.
6. Check notifications as **User B** — a "liked your post" notification should appear.

---

## Project Structure
```
accounts/       # CustomUser model, follow/unfollow logic, and authentication
posts/          # Post and Like models, feed logic, and content management
notifications/  # Generic notification system using ContentTypes
```