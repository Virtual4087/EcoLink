from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    pass

class Campaign(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    area = models.CharField(max_length=50)
    target = models.CharField(max_length=200)
    attendees = models.ManyToManyField(User, related_name="joined_events")
    contact_no = models.IntegerField(null=True)
    chat_room_link = models.CharField(max_length=100, null=True)
