from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


# create a custom user model
# derived from the AbstractBaseUser
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # objects = UserProfileManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    def get_fullname(self) -> str:
        """Retrieve fullname of user"""
        return self.name

    def get_shortname(self) -> str:
        """Retrieve shortname of user"""
        return self.name

    def __str__(self) -> str:
        """Return string representation of our user"""
        return self.email
