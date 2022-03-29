# Generated by Django 4.0.3 on 2022-03-07 10:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UCI_App', '0021_delete_loginlogoutlog'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLogoutLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=100)),
                ('host', models.CharField(max_length=100)),
                ('login_time', models.DateTimeField(blank=True, null=True)),
                ('logout_time', models.DateTimeField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Entrada o Salida',
                'verbose_name_plural': 'Entradas y Salidas',
                'db_table': 'Entradas y Salidas',
            },
        ),
    ]
