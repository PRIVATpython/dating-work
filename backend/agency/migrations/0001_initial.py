# Generated by Django 2.2.4 on 2019-09-26 07:16

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.TextField(help_text='Name', max_length=250, verbose_name='Name')),
                ('director', models.TextField(max_length=250, verbose_name='Name and Surname of the Boss')),
                ('login', models.TextField(help_text='Login', max_length=250, verbose_name='Login')),
                ('adress', models.TextField(help_text='Adress', max_length=250, verbose_name='Ardess of the office')),
                ('payment_method', models.CharField(choices=[('pb', 'Privatbank'), ('epay', 'Epay')], default='pb', max_length=50, verbose_name='Language')),
                ('contact_email', models.TextField(max_length=250, verbose_name='Email')),
                ('skype', models.TextField(max_length=250, verbose_name='Email')),
                ('other_messanger', models.TextField(help_text='Skype, telegram etc...', max_length=250, verbose_name='Other messangers')),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('city', models.TextField(max_length=250, verbose_name='City')),
                ('phone1', models.TextField(max_length=250, verbose_name='Phone 1')),
                ('phone2', models.TextField(max_length=250, verbose_name='Phone 2')),
                ('term', models.TextField(max_length=250, verbose_name='Term of work')),
                ('is_approved', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AgencyFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='agency_files')),
                ('video', models.FileField(upload_to='agency_files')),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agency.Agency')),
            ],
        ),
    ]
