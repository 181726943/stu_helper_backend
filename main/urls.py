from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import bookinfo, classroom, exam_info, grades, schedule, personalinfo, selectcourse, stu_class, get_csrftoken

router = DefaultRouter()
# router.register(r'user', viewset=login.UserViewSet)
router.register(r'bookinfo', viewset=bookinfo.BookInfoViewSet)
router.register(r'classroom', viewset=classroom.ClassRoomViewSet)
router.register(r'exam', viewset=exam_info.ExamInfoViewSet)
router.register(r'grade', viewset=grades.GradeViewSet)
router.register(r'personal', viewset=personalinfo.PersonalViewSet)
router.register(r'timetable', viewset=schedule.ScheduleViewSet)
router.register(r'select', viewset=selectcourse.SelectViewSet)
router.register(r'stuclass', viewset=stu_class.StuClassViewSet)


app_name = 'main'
urlpatterns = [
    # restful接口
    path('', include(router.urls)),
    # csrf防护接口
    path('getCsrftoken/', get_csrftoken.getcsrftoken),
    # 登录接口
    path('login/', include('dj_rest_auth')),
]
