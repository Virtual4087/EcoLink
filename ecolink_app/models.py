from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.
class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions')

class Campaign(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    area = models.CharField(max_length=50)
    target = models.CharField(max_length=200)
    attendees = models.ManyToManyField(User, related_name="joined_events")

