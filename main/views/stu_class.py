from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ValidationError

from main.models import StuClass, UserInfo
from main.serializers import StuClassSerializer


class StuClassViewSet(viewsets.ModelViewSet):
    query = StuClass.objects.all()
    serializer_class = StuClassSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['cou_arr']

    def create(self, request, *args, **kwargs):
        user = self.request.user
        try:
            uid = int(request.data['student'])
            tableid = int(request.data['cou_arr'])
        except:
            raise ValidationError(detail="参数错误")

        # 只允许本用户添加属于自己课程
        if uid != user.id:
            raise ValidationError(detail="不允许代替选课!")
        exist_objs = StuClass.objects.filter(student=user, educlass__id=tableid)
        if len(exist_objs) > 0:
            raise ValidationError(detail="你已经选过这门课了，不可以重复选课")
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        user = self.request.user
        ins = self.get_object()
        # ins = PeopleClass()
        if ins.student.id != user.id and user.identity == UserInfo.IdentityChoice.STUDENT:
            raise ValidationError(detail="禁止删除不属于你的课程")
        return super().destroy(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.identity == UserInfo.IdentityChoice.STUDENT:
            objs = StuClass.objects.filter(student=user)
        else:
            objs = StuClass.objects.filter(cou_arr__course_name__teacher=user)

        return objs
