from rest_framework import permissions

class CustomReadOnly(permissions.BasePermission):
    # GET : Pass All, PUT/PATCH : pass only current user
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user