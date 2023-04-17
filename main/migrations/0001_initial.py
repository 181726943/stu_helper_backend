# Generated by Django 2.2.10 on 2023-04-17 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(default='', max_length=100, verbose_name='图书名称')),
                ('rtype', models.CharField(choices=[('已读', '已读'), ('在读', '在读')], default='', max_length=10, verbose_name='阅读情况')),
                ('brdate', models.DateField(verbose_name='借阅时间')),
                ('redate', models.DateField(blank=True, verbose_name='归还时间')),
            ],
            options={
                'db_table': 'bookinfo',
            },
        ),
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=100, verbose_name='课程名称')),
                ('grade', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='成绩')),
                ('credit', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='学分')),
                ('gpa', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='绩点')),
            ],
            options={
                'db_table': 'score',
            },
        ),
    ]
