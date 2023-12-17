from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    pass

class City(models.Model):
    city = models.CharField(max_length=20)

class Campaign(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="city_campaigns")
    area = models.CharField(max_length=50)
    target = models.CharField(max_length=200)
    attendees = models.ManyToManyField(User, related_name="joined_events")
    contact_no = models.IntegerField(null=True)
