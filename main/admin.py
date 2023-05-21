from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserInfo, Course, ClassRoom, Course_arrang, StuClass, ExamInfo, Score, Bookinfo

# Register your models here.

admin.site.site_title = "校园助手"
admin.site.site_header = "校园助手"
admin.site.index_header = "校园助手管理"


@admin.register(UserInfo)
class UserModelAdmin(UserAdmin):
    # 列表页显示哪些字段
    list_display = ('username', 'user_name', 'institute', 'grade', 'profession', 'phone', 'identity')
    # 列表页中可编辑字段
    list_editable = ('identity', 'user_name', 'phone')
    # 过滤器
    list_filter = ('identity', 'is_superuser')
    # 搜索字段
    search_fields = ('user_name', 'username')
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "user_name", "identity", "password1", "password2"),
            }
        ),
    )


@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    # 列表页显示哪些字段
    list_display = ['id', 'course_name', 'teacher', 'credit']
    # 控制列表页可以链接到修改页的字段
    list_display_links = ['course_name']


@admin.register(ClassRoom)
class ClassRoomModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'building_name', 'room_num']
    list_filter = ['building_name']


@admin.register(Course_arrang)
class TimetableModelAdmin(admin.ModelAdmin):
    list_display = ['course_name', 'school_year', 'term', 'weekday', 'start_class', 'end_class', 'addr']
    list_filter = ['school_year', 'term']
    list_display_links = ['course_name']
    search_fields = ['course_name']


@admin.register(StuClass)
class StuClassModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'student', 'cou_arr']
    list_filter = ['cou_arr']
    search_fields = ['student__user_name']


@admin.register(ExamInfo)
class ExamInfoModelAdmin(admin.ModelAdmin):
    list_display = ['cou_arr', 'exam_date', 'begin_time', 'end_time', 'exam_addr']
    list_filter = ['cou_arr']
    search_fields = ['course_name']


@admin.register(Score)
class ScoreModelAdmin(admin.ModelAdmin):
    list_display = ['stu_name', 'grade', 'cou_arr', 'gpa']
    list_filter = ['cou_arr']
    search_fields = ['stu_name__user_name']
    list_per_page = 10


@admin.register(Bookinfo)
class BookinfoModelAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'stu_name', 'borrow_date', 'return_date', 'read_type']
    list_filter = ['read_type']
    search_fields = ['book_name']
