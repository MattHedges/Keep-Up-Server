from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from keepupapi.models import FreeTime
from rest_framework.decorators import action


class FreeTimeView(ViewSet):
    """Level up exercise view"""

    def retrieve(self, request, pk):
        freetime = FreeTime.objects.get(pk=pk)
        serializer = FreeTimeSerializer(freetime)
        return Response(serializer.data)
    
    class FreeTimeSerializer(serializers.ModelSerializer):
    """JSON serializer for exercise
    """
    class Meta:
        model = FreeTime
        fields = ('id', 'user', 'date', 'time' )
        depth = 1