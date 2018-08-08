# Generated by Django 2.0.7 on 2018-07-11 03:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='current_user',
            field=models.ForeignKey(null=True, on_delete='cascade', related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
