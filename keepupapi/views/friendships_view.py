from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from keepupapi.models import Friend
from rest_framework.decorators import action
from django.contrib.auth.models import User

class FrienshipView(ViewSet):

    def retrieve(self, request, pk):
        friend = Friend.objects.get(pk=pk)
        serializer = FriendSerializer(friend)
        return Response(serializer.data)

    def destroy(self, request, pk):
        friend = Friend.objects.get(pk=pk)
        friend.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class FriendSerializer(serializers.ModelSerializer):

    class Meta:
        model = Friend
        fields = ('id', 'user1', 'user2', 'are_friends', 'timestamp' )
        depth = 1