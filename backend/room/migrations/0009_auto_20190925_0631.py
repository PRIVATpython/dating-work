# Generated by Django 2.2.4 on 2019-09-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0008_auto_20190925_0626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chatcontact',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='chatcontact',
            name='is_suspended',
        ),
        migrations.AddField(
            model_name='chatroom',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='is_suspended',
            field=models.BooleanField(default=False),
        ),
    ]
