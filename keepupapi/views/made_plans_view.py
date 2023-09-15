from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from keepupapi.models import MadePlan
from rest_framework.decorators import action
from django.contrib.auth.models import User


class MadePlansView(ViewSet):
    """Level up madeplan view"""

    def retrieve(self, request, pk):
        madePlan = MadePlan.objects.get(pk=pk)
        serializer = MadePlanSerializer(madePlan)
        return Response(serializer.data)

    def update(self, request, pk):

        creator = User.objects.get(pk=request.data["user"])

        madePlan = MadePlan.objects.get(pk=pk)
        creator = creator
        madePlan.date = request.data["date"]
        madePlan.time = request.data["time"]
        madePlan.place = request.data["place"]

        madePlan.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        madeplan = MadePlan.objects.get(pk=pk)
        madeplan.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class MadePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MadePlan
        fields = ('id', 'creator', 'attendee', 'date', 'time', 'place' )
        depth = 1
