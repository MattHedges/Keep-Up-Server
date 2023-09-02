from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from keepupapi.models import FreeTime
from rest_framework.decorators import action
from django.contrib.auth.models import User


class FreeTimeView(ViewSet):
    """Level up freetime view"""

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

    def update(self, request, pk):
        user = User.objects.get(pk=request.data["user"])


        freetime = FreeTime.objects.get(pk=pk)
        user = user
        freetime.name = request.data["name"]
        freetime.date = request.data["date"]
        freetime.time = request.data["time"]

        freetime.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        if "user" in request.query_params:
            freetime = FreeTime.objects.filter(user_id=request.query_params['user'])
        elif "freetimeuser" and "freetime" in request.query_params:
            userFreetime = Freetime.objects.filter(user_id=request.query_params['freetimeuser'])
            freetime = userFreetime.filter(name=request.query_params['freetime'])
        else:
            freetime = Freetime.objects.all()
        serializer = FreetimeSerializer(freetime, many=True)
        return Response(serializer.data)

    def destroy(self, request, pk):
        freetime = FreeTime.objects.get(pk=pk)
        freetime.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FreeTimeSerializer(serializers.ModelSerializer):

    class Meta:
        model = FreeTime
        fields = ('id', 'user', 'date', 'time' )
        depth = 1