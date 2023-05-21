from rest_framework.decorators import action
from django.utils.datastructures import MultiValueDictKeyError
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import Course_arrang, ClassRoom
from main.serializers import TimetableSerializer


class SelectViewSet(viewsets.ModelViewSet):
    queryset = Course_arrang.objects.all()
    serializer_class = TimetableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course_name', 'school_year', 'term']

    # 选课信息查询
    @action(detail=False)
    def courseselect(self, request: Request, *args, **kwargs):
        try:
            term = int(request.query_params['term'])
            school_year = int(request.query_params['school_year'])
        except MultiValueDictKeyError:
            return Response({}, status=404)
        except Exception as e:
            return Response({}, status=404)

        if term and school_year:
            objs = Course_arrang.objects.filter(term=term, school_year=school_year)
        else:
            return Response([])
        res = []
        for timetable in objs:
            stuclass_set = timetable.stuclass_set.filter(student=self.request.user)
            selected = False
            stuid = -1
            if len(stuclass_set) > 0:
                selected = True
                stuid = stuclass_set.all()[0].id
            res.append({
                "table_id": timetable.pk,
                "cname": timetable.course_name.course_name,
                "credit": timetable.course_name.credit,
                "location": str(timetable.addr),
                "teacher": timetable.course_name.teacher.user_name,
                "selected": selected,
                "pcs_id": stuid,
            })
        return Response(res)
