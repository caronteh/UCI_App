# Generated by Django 4.0.3 on 2022-03-31 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UCI_App', '0060_alter_numhits_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conexiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conexion', models.CharField(default='Desconectado', max_length=15)),
                ('nombre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
