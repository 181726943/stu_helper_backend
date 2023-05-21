import random

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
        alldict = {}  # 所有课程查询字典

        user = self.request.user
        year = int(self.request.query_params['year'])
        term = int(self.request.query_params['term'])

        # 构造全部课程查询字典
        alldict['student'] = user
        alldict['cou_arr__school_year'] = year
        alldict['cou_arr__term'] = term

        color = ['red', 'orange', 'olive', 'green', 'cyan', 'blue', 'purple', 'mauve', 'pink', 'brown']
        index = -1

        my_class = StuClass.objects.filter(**alldict)
        res = []
        for cls in my_class:
            index = index if index < 10 else -1
            index += 1
            m_table = cls.cou_arr
            m_course = m_table.course_name
            weeks = [i for i in range(m_table.start_week, m_table.end_week + 1)]
            course = {
                'cname': m_course.course_name,
                'addr': str(m_table.addr),
                'teacher': m_course.teacher.user_name,
                'sumweek': len(weeks),   # 总周数
                'weeks': weeks,  # 上课周数，数组
                'start_week': m_table.start_week,  # 开始周
                'end_week': m_table.end_week,  # 结束周
                "weekday": m_table.weekday,  # 星期几上课
                'start_class': m_table.start_class,  # 课程开始节数
                'end_class': m_table.end_class,  # 课程结束节数
                'c_duration': m_table.end_class - m_table.start_class,  # 课程时长
                'bg': color[index],  # 背景色
            }
            res.append(course)
        return Response(res)

    @action(detail=False)
    def today(self, request: Request, *args, **kwargs):
        todaydict = {}  # 今日课程查询字典

        user = self.request.user
        year = int(self.request.query_params['year'])
        term = int(self.request.query_params['term'])
        weekday = self.request.query_params['weekday']  # 周几
        week = self.request.query_params['week']  # 第几周

        # 构造今日课程查询字典
        todaydict['student'] = user
        todaydict['cou_arr__school_year'] = year
        todaydict['cou_arr__term'] = term
        if weekday and week:
            todaydict['cou_arr__weekday'] = weekday
            todaydict['cou_arr__start_week__lte'] = week
            todaydict['cou_arr__end_week__gte'] = week

        # 今日课程的queryset对象
        today = StuClass.objects.filter(**todaydict)

        color = ['red', 'orange', 'olive', 'green', 'cyan', 'blue', 'purple', 'mauve', 'pink', 'brown']
        index = 10

        res = []
        for cou in today:
            index = index if index > -1 else 10
            index -= 1
            table = cou.cou_arr
            course = table.course_name
            detail = {
                'cname': course.course_name,
                'addr': str(table.addr),
                'teacher': course.teacher.user_name,
                'start_class': table.start_class,
                'end_class': table.end_class,
                'bg': color[index],
            }
            res.append(detail)
        return Response(res)
