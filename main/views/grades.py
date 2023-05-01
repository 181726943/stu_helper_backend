import json

from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import Score
from main.serializers import ScoreSerializer


class GradeViewSet(viewsets.ModelViewSet):
    query = Score.objects.all()
    serializer_class = ScoreSerializer

    @action(detail=False)
    def my_score(self, request: Request, *args, **kwargs):
        user = self.request.user
        myscore = Score.objects.filter(educlass__peopleclass__student=user)
        res = [{
            "cname": score.cou_arr.course_name.course_name,
            "credit": score.cou_arr.course_name.credit,
            "gpa": 0 if score.grade < 60 else (score.grade - 50) / 10,
            "scores": score.grade,
        } for score in myscore]
        return Response(res)

# def grades(request):
#
#     # 查询字典
#     data_dict = {}
#
#     # 获取用户id
#     stu_num = request.session['info']['stu_num']
#
#     # 将用户id加入查询字典
#     data_dict['stu_num'] = stu_num
#
#     yt_choice = request.GET
#     # print(type(yt_choice))
#     # print(yt_choice)
#     # 学年
#     xn = yt_choice.get('year', '')
#     # 学期
#     xq = yt_choice.get('term', '')
#     if xn:
#         data_dict['year'] = int(xn)
#     if xq:
#         data_dict['term'] = int(xq)
#     """
#     分页
#     """
#
#     # 这种方式获取到对象
#     grade_list = models.Score.objects.filter(**data_dict)
#     # # 获取到字典
#     # grade_dict = models.Score.objects.filter(**data_dict).values('cname', 'grade', 'gpa', 'credit')
#     # # 对象列表[obj, obj, obj]
#     # grade_obj_list = models.Score.objects.all()
#     # # 字典列表 [{'id':1, 'xxx': "xx"}, {'id':1, 'xxx': "xx"}]
#     # grade_dict_list = models.Score.objects.all().values('cname', 'grade', 'gpa', 'credit')
#     # # 元组列表 [('id', 1), ('xxx', "xx"),]
#     # grade_tuple_list = models.Score.objects.all().values_list('cname', 'grade', 'gpa', 'credit')
#
#     page_object = Page_init(request, grade_list)
#     page_grade_list = page_object.page_queryset
#     grade_page = page_object.html()
#
#     # 选择学年和学期
#     choose_Y_T = ScoreForm()
#     # 根据数据库中学年设置学年选择列表
#     year_select = models.Score.objects.values('year').distinct()
#     term_select = models.Score.objects.values('term').distinct()
#
#     context = {"grade_list": page_grade_list,  # 分页数据
#                "choose_Y_T": choose_Y_T,  # 学年学期生成器
#                "year_now": year_select,  # 学年选择表
#                "term_select": term_select,  # 学期选择列表
#                "date_dict": data_dict,  # 包含学年学期的字典
#                "grade_page": grade_page,  # 页码
#                "current_page": page_object.current_page  # 当前页
#                }
#
#     # list_grade = serializers.serialize("json", grade_list)
#     # return HttpResponse(list_grade)
#     return render(request, 'grades.html', context)
