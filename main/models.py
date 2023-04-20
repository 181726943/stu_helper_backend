from django.db import models


class UserInfo(models.Model):
    dorm_choice = (
        ("A", "A栋"),
        ("B", "B栋"),
        ("C", "C栋"),
        ("D", "D栋"),
        ("E", "E栋"),
        ("4", "4栋"),
        ("5", "5栋"),
        ("6", "6栋"),
    )
    stu_num = models.CharField("学号", max_length=15, primary_key=True)
    user = models.CharField("姓名", max_length=50, blank=False)
    password = models.CharField("密码", max_length=20, blank=False, default='123456')
    grade = models.PositiveIntegerField("年级")
    dorm_build = models.CharField("宿舍楼", max_length=5, choices=dorm_choice, default='')
    dorm_num = models.PositiveIntegerField("宿舍号")
    institute = models.CharField("学院", max_length=100, default='')

    class Meta:
        db_table = "personal"

    # 展示学号
    # def __str__(self):
    #     return self.stu_num


class score(models.Model):
    term_choice = (
        (0, "全部"),
        (1, "第一学期"),
        (2, "第二学期"),
    )
    stu_num = models.ForeignKey(related_name="学号", to="UserInfo", on_delete=models.CASCADE)
    year = models.IntegerField("学年", default=2019)
    term = models.SmallIntegerField("学期", choices=term_choice, default=1)
    cname = models.CharField("课程名称", max_length=100, default='')
    grade = models.DecimalField("成绩", max_digits=4, decimal_places=2, default=0.0)
    credit = models.DecimalField("学分", max_digits=2, decimal_places=1, default=0.0)
    gpa = models.DecimalField("绩点", max_digits=2, decimal_places=1, default=0.0)

    class Meta:
        db_table = "score"


class bookinfo(models.Model):
    book_choice = (
        ("已读", "已读"),
        ("在读", "在读"),
    )
    stu_num = models.ForeignKey(related_name="图书_学号", to="UserInfo", on_delete=models.CASCADE)
    book_name = models.CharField("图书名称", max_length=100, default='')
    read_type = models.CharField("阅读情况", max_length=10, choices=book_choice, default='')
    borrow_date = models.DateField("借阅时间", blank=False)
    return_date = models.DateField("归还时间", blank=True)

    class Meta:
        db_table = "bookinfo"


class timetable(models.Model):
    stu_num = models.ForeignKey(related_name="课表_学号", to="UserInfo", on_delete=models.CASCADE)
    course_name = models.CharField("课程名称", max_length=50, default='')
    addr = models.CharField("上课地点", max_length=20, default='')
    c_week = models.SmallIntegerField("上课时间(周次)")
    c_period = models.CharField("课节", max_length=10, default='')
    tech_name = models.CharField("教师姓名", max_length=50, default='')

    class Meta:
        db_table = "timetable"
