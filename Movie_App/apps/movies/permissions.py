from rest_framework.permissions import BasePermission


class IsAdminOrOwner(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated and request.user.is_admin:
            return True
        return obj.added_by == request.user