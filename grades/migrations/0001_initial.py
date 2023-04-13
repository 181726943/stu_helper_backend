# Generated by Django 2.2.10 on 2023-04-13 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(default='', max_length=100, verbose_name='课程名称')),
                ('grade', models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='成绩')),
                ('credit', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='学分')),
                ('gpa', models.DecimalField(decimal_places=1, default=0.0, max_digits=2, verbose_name='绩点')),
            ],
        ),
    ]