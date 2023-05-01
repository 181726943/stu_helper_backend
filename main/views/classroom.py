from rest_framework import viewsets

from main.models import ClassRoom
from main.serializers import ClassRoomSerializer
from main.permission import UserIdentity


class ClassRoomViewSet(viewsets.ModelViewSet):
    permission_classes = (UserIdentity,)
    query = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
