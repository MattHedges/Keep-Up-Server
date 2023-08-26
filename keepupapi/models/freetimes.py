from django.db import models
from django.contrib.auth.models import User

class FreeTime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date =  models.DateField(null=False)
    time = models.TimeField(null=True, blank=True)