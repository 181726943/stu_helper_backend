from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import (
    UserInfo,
    Course,
    ClassRoom,
    Course_arrang,
    StuClass,
    ExamInfo,
    Score,
    Bookinfo
)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['url', 'identity', 'username', 'user_name', 'institute', 'grade', 'profession', 'phone', 'email']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        exclude = ['id',]


class ClassRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassRoom
        field = "__all__"
        exclude = ['id',]


class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_arrang
        field = "__all__"
        exclude = ['school_year', 'term', 'id']


class StuClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = StuClass
        field = "__all__"

    def to_representation(self, instance):
        origin = super().to_representation(instance)
        extend = {
            "stu_name": instance.student.user_name,
            "profession": instance.student.profession,
            "grade": instance.student.grade
        }
        origin.update(extend)
        return origin


class ExamInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamInfo
        field = "__all__"
        exclude = ['id']


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        field = "__all__"
        exclude = ['id', 'year', 'term']


class BookinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookinfo
        field = "__all__"
        exclude = ['id']
