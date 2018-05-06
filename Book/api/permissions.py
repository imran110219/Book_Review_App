from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        # member = Membership.objects.get(user=user.request)
        # member.is_active
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user