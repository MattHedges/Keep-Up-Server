from django.db import models
from django.contrib.auth.models import User

class PotentialPlan(models.Model):
    idea = models.CharField(max_length=500)
    location = models.CharField(max_length=50)
    date = models.DateField(null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    invitees = models.ManyToManyField(User)