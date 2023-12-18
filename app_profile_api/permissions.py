from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # check if the request in the SAFE_METHODS
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if the request is coming from the owner
        return obj.id == request.user.id
