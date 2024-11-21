from .permissions import IsStaffPermissions
from rest_framework import permissions

class StaffPermissionsMixin():
    permission_classes =[permissions.IsAdminUser,IsStaffPermissions]