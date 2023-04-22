from django.shortcuts import render

from main.utils.form import ScoreForm

from main import models


def grades(request):
    # 补充成绩查询功能

    data_dict = {}
    # 学年
    xn = request.GET.get('year', '')
    # 学期
    xq = request.GET.get('term', '')
    if xn:
        data_dict['year'] = int(xn)
    if xq:
        data_dict['term'] = int(xq)
    """
    分页
    """
    from main.utils.page_init import Page_init

    grade_list = models.score.objects.filter(**data_dict)

    page_object = Page_init(request, grade_list)
    page_grade_list = page_object.page_queryset
    grade_page = page_object.html()

    # 选择学年和学期
    choose_Y_T = ScoreForm()
    # 根据数据库中学年设置学年选择列表
    year_select = models.score.objects.values('year').distinct()
    term_select = models.score.objects.values('term').distinct()

    context = {"grade_list": page_grade_list,  # 分页数据
               "choose_Y_T": choose_Y_T,  # 学年学期生成器
               "year_now": year_select,  # 学年选择表
               "term_select": term_select,  # 学期选择列表
               "date_dict": data_dict,  # 包含学年学期的字典
               "grade_page": grade_page,  # 页码
               "current_page": page_object.current_page  # 当前页
               }

    return render(request, 'grades.html', context)
