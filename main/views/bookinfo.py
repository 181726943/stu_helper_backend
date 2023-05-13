from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from main.serializers import BookinfoSerializer
from main.models import Bookinfo


class BookInfoViewSet(viewsets.ModelViewSet):
    queryset = Bookinfo.objects.all()
    serializer_class = BookinfoSerializer

    @action(detail=False)
    def readinfo(self, request: Request, *args, **kwargs):
        user = self.request.user
        begin_date = self.request.query_params['begin_date']
        end_date = self.request.query_params['end_date']
        my_reads = Bookinfo.objects.filter(stu_name=user, borrow_date__gte=begin_date, borrow_date__lte=end_date).\
            order_by("borrow_date")
        res = []
        for read in my_reads:
            res.append({
                "bookname": read.book_name,
                "borrow_date": read.borrow_date,
                "return_date": read.return_date,
                "read_type": read.get_read_type_display(),
            })
        return Response(res)


