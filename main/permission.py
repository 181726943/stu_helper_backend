from rest_framework import permissions


class UserIdentity(permissions.BasePermission):
    """
    自定义权限：依据身份分配权限
    学生可以查看所有属于自己的信息
    老师可以查看所有自己的信息，可以修改部分课程信息（地点，时间），可以增加成绩信息
    管理员拥有所有权限
    """
    def has_permission(self, request, view):
        identity = request.query_params['identity']

    def has_object_permission(self, request, view, obj):
        """
        # 分配权限
        :param request:
        :param view:
        :param obj:
        :return: bool
        """
        # identity = request.query_params['identity']
        # # 学生拥有只读权限
        # if identity == 1 and request.method in permissions.SAFE_METHODS:
        #     return True
        # # 教师拥有部分修改权限
        # elif identity == 2 and request.username == obj.username:
        #     return True
        # # 管理员拥有所有权限
        # elif identity == 3:
        #     return True
        return False
