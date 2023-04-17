from django.db import models


# Create your models here.

class score(models.Model):
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
    book_name = models.CharField("图书名称", max_length=100, default='')
    read_type = models.CharField("阅读情况", max_length=10, choices=book_choice, default='')
    borrow_date = models.DateField("借阅时间", blank=False)
    return_date = models.DateField("归还时间", blank=True)

    class Meta:
        db_table = "bookinfo"




