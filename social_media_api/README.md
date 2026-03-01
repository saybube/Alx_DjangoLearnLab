# Social Media API Documentation

This project provides a backend REST API for a social media platform, built using Django and the Django REST Framework (DRF). The system handles user authentication, profile management, and social relationship tracking.

---

## Technical Overview: User Model
The application implements a **Custom User Model** by extending Django's `AbstractUser`. This approach provides the flexibility required for social media features while maintaining compatibility with Django’s built-in authentication system.

### Custom Fields
| Field | Type | Description |
| :--- | :--- | :--- |
| `bio` | TextField | Stores user biographical information (optional). |
| `profile_picture` | ImageField | Stores user avatar images in the `profile_pics/` directory. |
| `followers` | ManyToManyField | A self-referential relationship used to track user connections (symmetrical=False). |



---

## Installation and Environment Setup

### 1. Repository Configuration
Navigate to the project directory and initialize the environment:
```bash
python -m venv venv
source venv/Scripts/activate 

