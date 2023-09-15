from django.db import models
from django.contrib.auth.models import User

class MadePlan(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator'),
    attendee = models.ManyToManyField(User, through=User)
    date = models.DateField(null=False)
    time = models.TimeField
    place = models.CharField(null=False, max_length=100)