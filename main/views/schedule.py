from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import Course, StuClass, UserInfo
from main.serializers import CourseSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    query = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False)
    def my_course(self, request: Request, *args, **kwargs):
        user = self.request.user
        my_class = StuClass.objects.filter(student=user)
        res = []
        for cls in my_class:
            m_table = cls.cou_arr
            m_course = m_table.course_name
            zcd = [i for i in range(m_table.start_week, m_table.end_week + 1)]
            course = {
                'cname': m_course.course_name,
                'addr': str(m_table.classroom),
                'teacher': m_course.teacher.user_name,
                'zcdd': len(zcd),
                'zcd': zcd,
                "weekday": m_table.weekday,
                'jcs': m_table.start_class,
                'c_duration': m_table.end_class - m_table.start_class,  # 课程时长
                'bg': 'blue'
            }
            res.append(course)
        return Response(res)

    # 获取老师发布的课程
    @action(detail=False)
    def getcoursebyme(self, request: Request, *args, **kwargs):
        user = self.request.user
        # 学生无权限获取
        if user.identity != UserInfo.IdentityChoice.TEACHER:
            raise ValidationError(detail="非老师无法获取")
        # res = []
        objs = Course.objects.filter(teacher=user)
        r = CourseSerializer(objs, many=True)
        return Response(r.data)

