from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class IsStaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
    ]


class UserQuerySetMixin():
    user_field = 'user'

    def get_queryset(self, *args, **kwargs):
        lookup_data = {}
        allow_staff_view = False
        user = self.request.user
        lookup_data[self.user_field] = user
        # print(lookup_data)
        qs = super().get_queryset(*args, **kwargs)
        if allow_staff_view and user.is_staff:
        # print(qs)
            return qs
        return qs.filter(**lookup_data)