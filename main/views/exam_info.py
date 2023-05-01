from datetime import timedelta, datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import ExamInfo
from main.serializers import ExamInfoSerializer


class ExamInfoViewSet(viewsets.ModelViewSet):
    query = ExamInfo.objects.all()
    serializer_class = ExamInfoSerializer
    td_bj = timedelta(hours=8)

    @action(detail=False)
    def myexam(self, request: Request, *args, **kwargs):
        user = self.request.user
        # exams = ExamInfo.objects.filter(timetable__stuclass__student=user)
        exams = ExamInfo.objects.filter(cou_arr__stuclass__student=user)
        now = datetime.utcnow() + self.td_bj
        res = []
        for exam in exams:
            # 硬编码了
            begin = datetime.utcfromtimestamp(exam.begin_time.timestamp())
            begin = begin + self.td_bj
            if begin < now:
                continue
            res.append({
                "cname": exam.cou_arr.course_name.course_name,
                "begin_time": begin.strftime("%Y-%m-%d %H:%M"),
                "restday": (begin - now).days,
                "exam_addr": str(exam.classroom)
            })
        return Response(res)
