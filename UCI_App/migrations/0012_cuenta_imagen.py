# Generated by Django 4.0.3 on 2022-03-03 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0011_alter_loginlogoutlog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='imagen',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
