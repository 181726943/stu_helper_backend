from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models
from django import forms
# from main.models import score, bookinfo, timetable
import datetime


class UserForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["stu_num", "password"]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.items():
                field.widgets.attrs = {"placeholder": field.label}


class ScoreForm(forms.ModelForm):
    class Meta:
        model = models.score
        fields = "__all__"

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.item():
                field.widgets.attrs = {"placeholder": field.labels}


class BookForm(forms.ModelForm):
    class Meta:
        model = models.bookinfo
        fields = ["book_name", "read_type", "borrow_date", "return_date"]


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = models.timetable
        fields = ["course_name", "addr", "c_period", "tech_name", "stu_num"]

        # widgets = {
        #     "course_name": forms.TextInput(attrs={"class": "form-control"})
        #     "addr": forms.TextInput(attrs={"class": "form-control"})
        # }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields.item():
                field.widgets.attrs = {"class": "form-control", "placeholder": field.labels}


def home(request):
    date = datetime.date.today().isoweekday()
    today_schedule = models.timetable.objects.filter(c_week=date)
    schedule = ScheduleForm()
    return render(request, "home.html", {'schedule': schedule})


def login(request):
    # 补充登录逻辑
    if request.method == 'GET':
        login_model = UserForm()
        return render(request, 'login.html', {"login_model": login_model})
    s_num = request.POST.get("stu_num")
    pwd = request.POST.get("pwd")
    users = models.UserInfo.objects.get(user=s_num)
    if pwd == users.password:
        return redirect('/main/home/')
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def grades(request):
    # 补充成绩查询功能
    date_now = datetime.date.today().year  # 当前年份

    data_dict = {}
    # 学年
    xn = request.GET.get('xn')
    # 学期
    xq = request.GET.get('term')
    if xn and xq:
        data_dict['year'] = xn
        data_dict['term'] = xq
    grade_list = models.score.objects.filter(**data_dict)
    print(grade_list)
    print(xq)
    print(data_dict)
    choose_Y_T = ScoreForm()
    year_now = models.score.objects.values('year').distinct()
    return render(request, 'grades.html',
                  {"grade_list": grade_list, "choose_Y_T": choose_Y_T, "year_now": year_now})


def timetable(request):
    return render(request, "timetable.html")


def bookinfo(request):
    return render(request, "bookinfo.html")


def personalinfo(request):
    """编辑/查看个人信息"""
    if request.method == "GET":
        pass
    return render(request, 'personalinfo.html')