# Generated by Django 4.2.7 on 2023-12-16 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecolink_app', '0002_campaign_delete_event'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='organizer',
        ),
    ]
