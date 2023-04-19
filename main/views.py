from django.shortcuts import render, redirect
from django.http import HttpResponse
from main import models
from django import forms
# from main.models import score, bookinfo, timetable
import datetime


class ScoreForm(forms.ModelForm):
    class Meta:
        model = models.score
        fields = ["year", "term"]


class BookForm(forms.ModelForm):
    class Meta:
        model = models.bookinfo
        fields = ["book_name", "read_type", "borrow_date", "return_date"]


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = models.timetable
        fields = ["course_name", "addr", "c_period", "tech_name"]

        # widgets = {
        #     "course_name": forms.TextInput(attrs={"class": "form-control"})
        #     "addr": forms.TextInput(attrs={"class": "form-control"})
        # }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            for name, field in self.fields:
                field.widgets.attrs = {"class": "form-control", "placeholder": field.labels}


def home(request):
    date = datetime.date.today().isoweekday()
    today_schedule = models.timetable.objects.filter(c_week=date)
    schedule = ScheduleForm()
    return render(request, "home.html", {'schedule': schedule})


def personalinfo(request):
    """编辑/查看个人信息"""
    if request.method == "GET":
        pass
    return render(request, 'personalinfo.html')


def login(request):
    # 补充登录逻辑
    if request.method == 'GET':
        print('method=get')
        return render(request, 'login.html')
    username = request.POST.get("user")
    pwd = request.POST.get("pwd")
    users = models.UserInfo.objects.get(user=username)
    if pwd == users.password:
        return render(request, 'home.html')
    return render(request, 'login.html', {"error_msg": "用户名或密码错误"})


def grades(request):
    # 补充成绩查询功能
    grade_list = models.score.objects.all()
    choose_Y_T = ScoreForm()
    year_now = datetime.date.year
    return render(request, 'grades.html', {"grade_list": grade_list, "choose_Y_T": choose_Y_T, "year_now": year_now})
