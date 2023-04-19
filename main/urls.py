from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    # 主页
    path('home/', views.home, name='home'),
    # 个人中心
    path('personalinfo/', views.personalinfo, name='personalinfo'),
    # 成绩查询
    path('grades/', views.grades, name='grades'),
]
