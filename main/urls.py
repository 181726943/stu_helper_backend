from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # 首页
    path('home/', views.home, name='home'),
    # 个人中心
    path('personalinfo/', views.personalinfo, name='personalinfo'),
    # 成绩查询
    path('grades/', views.grades, name='grades'),
    # 课表查询
    path('timetable/', views.timetable, name='timetable'),
    # 图书借阅情况
    path('bookinfo/', views.bookinfo, name='bookinfo'),
]
