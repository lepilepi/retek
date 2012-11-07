from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Contract(models.Model):
    restaurant = models.ForeignKey(Restaurant)
    agent = models.ForeignKey(User, related_name='added_contracts')
    contact = models.ForeignKey(User, related_name='contracts')

    duration = models.IntegerField()
    share = models.FloatField()

    timestamp = models.DateTimeField(auto_now_add=True)
