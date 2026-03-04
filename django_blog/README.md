# Django Blog Authentication System

## Overview

The authentication system for the `django_blog` project is built on Django's internal framework. It provides a secure environment for users to register, manage their identity, and interact with blog content.

---

## Authentication Components

### User Registration

- **Form** – Uses a `CustomUserCreationForm` that extends Django's `UserCreationForm` to include `email` as a required field.
- **Security** – Passwords are never stored in plain text. Django automatically hashes them using the PBKDF2 algorithm with a SHA256 hash.
- **Logic** – Located in `blog/views.py`. Validates user input, saves the new user to the database, and redirects to the login page.

### Login & Logout

- **Mechanism** – Utilizes Django's built-in class-based views (`LoginView` and `LogoutView`).
- **Session Management** – On login, a session cookie is stored in the user's browser, keeping them authenticated across pages.
- **CSRF Protection** – Every login attempt is protected by a CSRF token to ensure requests originate from the site.

### Profile Management

- **Access Control** – The profile page is protected by the `@login_required` decorator. Unauthenticated users are redirected to the login page.
- **Editing** – Users can update their `username` and `email` via a `ModelForm`. The view handles `POST` requests to update the `User` instance in the database.

---

## Testing the Features

| Feature | Test Instructions | Expected Result |
|---|---|---|
| **Registration** | Navigate to `/register/`, fill in username, email, and password, then click "Register". | Success message and redirect to the login page. |
| **Login** | Enter credentials at `/login/`. | Redirect to the home page or the URL set in `LOGIN_REDIRECT_URL`. |
| **Security (CSRF)** | Submit the login or registration form without `{% csrf_token %}` in the HTML. | Django returns a `403 Forbidden` error. |
| **Authorization** | While logged out, visit `http://127.0.0.1:8000/profile/`. | Automatic redirect to the login page. |
| **Profile Update** | Log in, go to `/profile/`, change your email, and click "Save". | Page refreshes with a success message and displays the updated email. |
| **Logout** | Click the Logout link or visit `/logout/`. | Session ends; `/profile/` is no longer accessible. |

---

## Technical Configuration

| Setting | Location | Purpose |
|---|---|---|
| URL Patterns | `blog/urls.py` | Defines auth routes, included in the main project URLs. |
| `LOGIN_REDIRECT_URL` | `settings.py` | Destination after a successful login. |
| `LOGOUT_REDIRECT_URL` | `settings.py` | Destination after logout. |