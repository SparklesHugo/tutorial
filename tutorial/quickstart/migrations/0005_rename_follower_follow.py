# Generated by Django 3.2 on 2021-04-23 08:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0004_auto_20210423_1655'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Follower',
            new_name='Follow',
        ),
    ]
