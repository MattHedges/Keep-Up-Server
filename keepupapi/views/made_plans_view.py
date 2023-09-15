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
        madeplan = MadePlan.objects.get(pk=pk)
        serializer = MadePlanSerializer(madeplan)
        return Response(serializer.data)
    


class MadePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MadePlan
        fields = ('id', 'creator', 'attendee', 'date', 'time', 'place' )
        depth = 1
