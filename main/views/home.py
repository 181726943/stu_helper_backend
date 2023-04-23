import datetime

from django.shortcuts import render,redirect

from main import models
from main.utils.form import ScheduleForm


def home(request):
    """主页"""

    # 检查用户是否已登录
    # 用户发来请求，获取cookie随机字符串，检查session中的字符串
    # log_status = request.session.get("info")
    # if not log_status:
    #     return redirect('/login/')

    date = datetime.date.today().isoweekday()
    today_schedule = models.timetable.objects.filter(weekday=date)
    schedule = ScheduleForm()
    return render(request, "home.html", {'schedule': schedule})
