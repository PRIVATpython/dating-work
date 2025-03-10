# Generated by Django 2.2.4 on 2019-09-09 18:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userprofile_is_online'),
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='abonent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='abonent', to='account.UserProfile'),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='account.UserProfile'),
        ),
    ]
