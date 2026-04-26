from rest_framework.permissions import BasePermission, IsAdminUser, SAFE_METHODS


class IsSelfOrAdmin(BasePermission):
    """Allow access only to the account owner or an admin user."""

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_staff
