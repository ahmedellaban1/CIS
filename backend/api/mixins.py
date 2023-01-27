from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class IsStaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
    ]