from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework import permissions


class IsOwnerOrReadOnly(BasePermission):

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user)


class IsAuthenticatedOrReadOnly(IsAuthenticated):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return super().has_permission(request, view)
