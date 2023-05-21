from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import ClassRoom, Course_arrang
from main.serializers import ClassRoomSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer

    # 空教室查询
    @action(detail=False)
    def roomsearch(self, request: Request, *args, **kwargs):
        searchdict = {}

        term = request.query_params['term']
        year = request.query_params['year']
        begin = int(request.query_params['begin'])  # 开始节数
        end = int(request.query_params['end'])  # 结束节数
        weekday = int(request.query_params['weekday'])  # 星期几
        weeks = int(request.query_params['weeks'])  # 哪一周
        build = request.query_params['build']  # 教学楼编号

        if term and year:
            searchdict['term'] = int(term)
            searchdict['school_year'] = int(year)
        searchdict['start_class'] = begin
        searchdict['end_class'] = end
        searchdict['weekday'] = weekday
        searchdict['start_week__lte'] = weeks
        searchdict['end_week__gte'] = weeks

        full = Course_arrang.objects.filter(**searchdict).distinct().values_list('addr', flat=True)
        empty = ClassRoom.objects.filter(building_name=build).exclude(id__in=full)

        res = []
        for room in empty:
            res.append({
                "build": room.building_name,
                "number": room.room_num,
            })
        return Response(res)
