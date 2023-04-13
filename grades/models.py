from django.db import models

# Create your models here.

class score(models.Model):
    cname = models.CharField("课程名称", max_length=100, default='')
    grade = models.DecimalField("成绩", max_digits=4, decimal_places=2, default=0.0)
    credit = models.DecimalField("学分", max_digits=2, decimal_places=1, default=0.0)
    gpa = models.DecimalField("绩点", max_digits=2, decimal_places=1, default=0.0)
