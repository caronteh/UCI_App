# Generated by Django 4.0.3 on 2022-03-02 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loginlogoutlog',
            name='session_key',
        ),
    ]
