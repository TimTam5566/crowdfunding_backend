from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission): # Custom permission class to allow only owners of an object to edit it.
    def has_object_permission(self, request, view, obj): # This method checks if the user has permission to perform the action on the object.
        if request.method in permissions.SAFE_METHODS: # SAFE_METHODS are GET, HEAD, and OPTIONS requests, which are read-only.
            return True
        else: 
            return obj.owner == request.user # For other request methods (like POST, PUT, DELETE), only the owner of the object has permission to perform actions.
        # This line checks if the owner of the object (obj.owner) is the same as the user making the request (request.user).
class IsSupporterOrReadOnly(permissions.BasePermission): # Custom permission class to allow only supporters of a pledge to edit it.
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.supporter == request.user
        