from rest_framework.permissions import BasePermission


class IsPostAdminOrSelf(BasePermission):

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user.is_authenticated and request.user.is_admin
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_admin:
            return True
        return obj == request.user