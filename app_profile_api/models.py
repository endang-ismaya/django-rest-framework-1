from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError("User must have an email address")

        # normalize email
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # hashed password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email=email, name=name, password=password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


# create a custom user model
# derived from the AbstractBaseUser
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

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
