# Generated by Django 4.0.3 on 2022-03-07 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0022_loginlogoutlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propuestas',
            old_name='hospital',
            new_name='opciones',
        ),
    ]