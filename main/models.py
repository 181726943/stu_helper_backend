from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.datetime_safe import date
from django.utils.translation import gettext_lazy as _


class UserInfo(AbstractUser):
    class IdentityChoice(models.IntegerChoices):
        STUDENT = 1, '学生'
        TEACHER = 2, '教师'
        ADMIN = 3, '管理员'

    identity = models.IntegerField("身份", choices=IdentityChoice.choices, default=IdentityChoice.STUDENT)
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        "学号/工号",
        max_length=150,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    user_name = models.CharField(verbose_name="姓名", max_length=50, blank=False)
    grade = models.PositiveIntegerField(verbose_name="年级", null=True, blank=True)
    institute = models.CharField(verbose_name="学院", max_length=100, null=True, blank=True)
    profession = models.CharField(verbose_name="专业", max_length=150, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True, verbose_name="手机号")

    class Meta(AbstractUser.Meta):
        db_table = "personal"

    # 显示身份和姓名
    def __str__(self):
        name = ""
        if self.identity == 1:
            name = "学生"
        elif self.identity == 2:
            name = "老师"
        else:
            name = "管理员"
        return f"{self.user_name} "


class Course(models.Model):
    # 课程id
    id = models.BigAutoField(primary_key=True, null=False)
    teacher = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name='任课老师')
    course_name = models.CharField(max_length=50, verbose_name="课程名称")
    credit = models.FloatField(verbose_name="课程学分")

    class Meta:
        db_table = "course"
        verbose_name = verbose_name_plural = "课程"

    def __str__(self):
        return f"{self.course_name}-{self.teacher.user_name}"


class ClassRoom(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    building_name = models.CharField(max_length=50, verbose_name="教学楼编号")
    room_num = models.PositiveIntegerField(verbose_name="教室编号")

    class Meta:
        db_table = "classroom"
        verbose_name = verbose_name_plural = "教室"

    def __str__(self):
        return f"{self.building_name}-{self.room_num}"


class Course_arrang(models.Model):
    class WeekChoice(models.IntegerChoices):
        Monday = 1, "星期一"
        Tuesday = 2, "星期二"
        Wednesday = 3, "星期三"
        Thursday = 4, "星期四"
        Friday = 5, "星期五"
        Saturday = 6, "星期六"
        Sunday = 7, "星期天"

    class TermChoice(models.IntegerChoices):
        one = 1, "第一学期"
        two = 2, "第二学期"
    id = models.BigAutoField(primary_key=True, null=False)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程名称")
    start_week = models.SmallIntegerField(verbose_name="课程开始周", default=1)
    end_week = models.SmallIntegerField(verbose_name="课程结束周", default=18)
    weekday = models.IntegerField(verbose_name="上课日", choices=WeekChoice.choices, blank=True)
    start_class = models.SmallIntegerField(verbose_name="开始节数", default=1)
    end_class = models.SmallIntegerField(verbose_name="结束节数", default=14)
    school_year = models.IntegerField(verbose_name="学年")
    term = models.IntegerField(verbose_name="学期", choices=TermChoice.choices)
    addr = models.ForeignKey(ClassRoom, max_length=20, on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name="上课地点")

    class Meta:
        verbose_name = verbose_name_plural = "课表"
        db_table = "course_arrange"

    def __str__(self):
        return f"{self.course_name}"


class StuClass(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    student = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="学生")
    cou_arr = models.ForeignKey(Course_arrang, on_delete=models.CASCADE, verbose_name="课程安排")

    class Meta:
        db_table = "stuclass"
        verbose_name = verbose_name_plural = "教学班成员"


class ExamInfo(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    cou_arr = models.ForeignKey(Course_arrang, on_delete=models.CASCADE, verbose_name="课程安排")
    exam_addr = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, verbose_name="考试地点")
    exam_date = models.DateField(verbose_name="考试日期", default=date.today)
    begin_time = models.DateTimeField(verbose_name="考试开始时间")
    end_time = models.DateTimeField(verbose_name="考试结束时间")

    class Meta:
        db_table = "ExamInfo"
        verbose_name = verbose_name_plural = "考试"

    def __str__(self):
        return f"{self.cou_arr.course_name}-{str(self.exam_addr)}-{str(self.exam_date)}"


class Score(models.Model):
    term_choice = (
        (1, "第一学期"),
        (2, "第二学期"),
    )
    stu_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="学生姓名")
    cou_arr = models.ForeignKey(Course_arrang, on_delete=models.CASCADE, verbose_name="课程")
    grade = models.DecimalField(verbose_name="成绩", max_digits=4, decimal_places=1, default=0.0)
    gpa = models.DecimalField(verbose_name="绩点", max_digits=2, decimal_places=1, default=0.0)

    class Meta:
        verbose_name = verbose_name_plural = "成绩"
        db_table = "score"


class Bookinfo(models.Model):
    book_choice = (
        (1, "已读"),
        (2, "在读"),
    )
    stu_name = models.ForeignKey(UserInfo, on_delete=models.CASCADE, verbose_name="读者姓名")
    book_name = models.CharField(verbose_name="图书名称", max_length=100, default='')
    read_type = models.IntegerField(verbose_name="阅读情况", choices=book_choice)
    borrow_date = models.DateField(verbose_name="借阅时间", blank=False)
    return_date = models.DateField(verbose_name="归还时间", blank=True)

    class Meta:
        verbose_name = verbose_name_plural = "图书借阅信息"
        db_table = "bookinfo"

    def __str__(self):
        return f"{self.book_name}-{str(self.borrow_date)}-{str(self.return_date)}"
