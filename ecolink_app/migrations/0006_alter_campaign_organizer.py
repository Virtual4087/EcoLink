# Generated by Django 4.2.7 on 2023-12-17 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecolink_app', '0005_remove_campaign_state_campaign_chat_room_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='organizer',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to='ecolink_app.user'),
        ),
    ]
