from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object level permission to only allow
    owners of post or comment to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
