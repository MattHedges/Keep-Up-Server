from django.contrib.auth.models import User
from django.db import models

class FriendshipRequest(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_sent')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_requests_received')
    is_approved = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)