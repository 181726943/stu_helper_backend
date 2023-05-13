from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import ExamInfo
from main.serializers import ExamInfoSerializer


class ExamInfoViewSet(viewsets.ModelViewSet):
    queryset = ExamInfo.objects.all()
    serializer_class = ExamInfoSerializer

    @action(detail=False)
    def myexam(self, request: Request, *args, **kwargs):

        search_dict = {}  # 查询参数

        user = self.request.user
        year = datetime.now().year  # 当前年份
        month = datetime.now().month  # 当前月份
        year = year if month >= 9 else year - 1  # 学年
        term = 1 if month >= 9 else 2  # 学期
        cname = self.request.query_params.get("cname")  # 课程名称

        search_dict["cou_arr__stuclass__student"] = user
        search_dict["cou_arr__school_year"] = year
        search_dict["cou_arr__term"] = term
        # 判断前端传过来的参数是否有值
        if cname:
            search_dict["cou_arr__course_name"] = cname

        exams = ExamInfo.objects.filter(**search_dict)

        res = []
        for exam in exams:
            res.append({
                "cname": exam.cou_arr.course_name.course_name,
                "exam_date": exam.exam_date.strftime("%Y-%M-%D"),
                "exam_time": exam.begin_time.strftime("%H:%M") + '-' + exam.end_time.strftime("%H %M"),
                "exam_addr": str(exam.classroom)
            })
        return Response(res)
