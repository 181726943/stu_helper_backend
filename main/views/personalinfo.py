from django.contrib.auth.models import Group
from django.db.models import F
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response

from main.models import UserInfo
from main.serializers import UserInfoSerializer, GroupSerializer


class PersonalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
