# Generated by Django 2.2.4 on 2019-09-26 10:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moderation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModerationFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='moderation_files')),
                ('moderation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moderation.Moderation')),
            ],
        ),
    ]
