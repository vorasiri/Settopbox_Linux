from django.db import models

# Create your models here.
class StateHolder(models.Model):
    mediaSharing = models.IntegerField(default=0)
    homeEntertain = models.IntegerField(default=0)
    peer2peer = models.IntegerField(default=0)
    controlDegree = models.IntegerField(default=0)
     
