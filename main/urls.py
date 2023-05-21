from dj_rest_auth.views import PasswordResetConfirmView, PasswordResetView
from django.urls import path, include
from rest_framework import routers
from django.conf.urls.static import static

from stu_helper import settings
from .views import bookinfo, classroom, exam_info, grades, schedule, personalinfo, selectcourse, stu_class, \
    get_csrftoken

router = routers.SimpleRouter()
router.register(r'bookinfo', bookinfo.BookInfoViewSet)
router.register(r'classroom', classroom.ClassRoomViewSet)
router.register(r'exam', exam_info.ExamInfoViewSet)
router.register(r'grade', grades.GradeViewSet)
router.register(r'user', personalinfo.PersonalViewSet)
router.register(r'timetable', schedule.ScheduleViewSet)
router.register(r'select', selectcourse.SelectViewSet)
router.register(r'stuclass', stu_class.StuClassViewSet)


urlpatterns = [
    # restful接口
    path('', include(router.urls)),
    # csrf防护接口
    path('getCsrftoken/', get_csrftoken.getcsrftoken),
    # 登录接口
    path('auth/', include('dj_rest_auth.urls')),

    path('password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
