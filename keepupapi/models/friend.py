from django.db import models
from django.contrib.auth.models import User


class Friend(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friends')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='_unused_friend_relation')
    timestamp = models.DateTimeField(auto_now_add=True) 