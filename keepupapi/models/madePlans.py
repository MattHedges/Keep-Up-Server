from django.db import models
from django.contrib.auth.models import User

class MadePlan(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    attendee = models.ManyToManyField(User, through=User)
    date = models.ForeignKey("freetime", related_name="date", on_delete=models.CASCADE)
    time = models.TimeField
    place = models.CharField(null=False, max_length=100)