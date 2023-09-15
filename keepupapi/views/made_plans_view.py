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

    def create(self, request):

        creator = User.objects.get(id=request.data["user"])
        attendee = User.objects.get(id=request.data["user"])

        madePlan = MadePlan.objects.create(
        creator = creator,
        attendee = attendee,
        date = request.data["date"],
        time = request.data["time"],
        place = request.data["place"]
        )
        serializer = MadePlanSerializer(madePlan)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):

        creator = User.objects.get(pk=request.data["user"])

        madePlan = MadePlan.objects.get(pk=pk)
        creator = creator
        madePlan.date = request.data["date"]
        madePlan.time = request.data["time"]
        madePlan.place = request.data["place"]

        madePlan.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

def list(self, request):
        query_params = request.query_params.dict()

        if 'attendee' in query_params:
            madePlans = MadePlan.objects.filter(attendee=query_params['attendee'])
        elif 'creator' in query_params:
            madePlans = MadePlan.objects.filter(creator = query_params['creator'])
        else:
            madePlans = MadePlan.objects.all()
        serializer = MadePlanSerializer(madePlans, many=True)
        return Response(serializer.data)


    def destroy(self, request, pk):
        madeplan = MadePlan.objects.get(pk=pk)
        madeplan.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)



class MadePlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = MadePlan
        fields = ('id', 'creator', 'attendee', 'date', 'time', 'place' )
        depth = 1
