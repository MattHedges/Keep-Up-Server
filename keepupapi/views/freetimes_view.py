from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from keepupapi.models import FreeTime
from rest_framework.decorators import action
from django.contrib.auth.models import User


class FreeTimeView(ViewSet):
    """Level up exercise view"""

    def retrieve(self, request, pk):
        freetime = FreeTime.objects.get(pk=pk)
        serializer = FreeTimeSerializer(freetime)
        return Response(serializer.data)
    
    def create(self, request):

        user = User.objects.get(id=request.data["user"])

        freetime = FreeTime.objects.create(
        user=user,
        date=request.data["date"],
        time=request.data["time"]
        )
        serializer = FreeTimeSerializer(freetime)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class FreeTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FreeTime
        fields = ('id', 'user', 'date', 'time' )
        depth = 1