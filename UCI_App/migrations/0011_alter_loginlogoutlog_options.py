# Generated by Django 4.0.3 on 2022-03-02 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0010_alter_loginlogoutlog_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loginlogoutlog',
            options={'verbose_name': 'Entrada o Salida', 'verbose_name_plural': 'Entradas y Salidas'},
        ),
    ]