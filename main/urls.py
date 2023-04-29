from django.urls import path
from . import views
from .views import home, personalinfo, grades, timetable, bookinfo

app_name = 'main'
urlpatterns = [
    # 首页
    path('home/', home.home, name='home'),
    # 个人中心
    path('personalinfo/', personalinfo.personalinfo, name='personalinfo'),
    # 成绩查询
    path('grades/', grades.grades, name='grades'),
    # 课表查询
    path('Timetable/', timetable.timetable, name='Timetable'),
    # 图书借阅情况
    path('Bookinfo/', bookinfo.bookinfo, name='Bookinfo'),
]
