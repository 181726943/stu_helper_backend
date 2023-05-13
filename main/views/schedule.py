from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import Course, StuClass, UserInfo
from main.serializers import CourseSerializer


class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=False)
    def my_course(self, request: Request, *args, **kwargs):
        user = self.request.user
        my_class = StuClass.objects.filter(student=user)
        res = []
        for cls in my_class:
            m_table = cls.cou_arr
            m_course = m_table.course_name
            weeks = [i for i in range(m_table.start_week, m_table.end_week + 1)]
            course = {
                'cname': m_course.course_name,
                'addr': str(m_table.addr),
                'teacher': m_course.teacher.user_name,
                'sumweek': len(weeks),   # 总周数
                'weeks': weeks,  # 上课周数，数组
                "weekday": m_table.weekday,  # 星期几上课
                'start_class': m_table.start_class,  # 课程开始节数
                'c_duration': m_table.end_class - m_table.start_class,  # 课程时长
                'bg': 'blue'
            }
            res.append(course)
        return Response(res)
