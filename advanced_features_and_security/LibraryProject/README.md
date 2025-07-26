# LibraryProject - Permissions and Groups Setup

## 🎯 Objective
Implement a permission-based access control system using Django’s built-in groups and custom model permissions to manage access to book-related views.

---

## 📦 App Structure
- Project: `LibraryProject`
- App: `bookshelf`

---

## 🔐 Permissions

Custom permissions are defined in the `Book` model:

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]
