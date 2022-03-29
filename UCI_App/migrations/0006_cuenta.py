# Generated by Django 4.0.3 on 2022-03-02 22:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UCI_App', '0005_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro', models.CharField(choices=[('JX', 'JX'), ('VH', 'VH')], max_length=15)),
                ('hospital', models.CharField(choices=[('JoanXXIII', 'JoanXXIII'), ('VallHebron', 'VallHebron')], max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
