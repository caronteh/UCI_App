# Generated by Django 4.0.3 on 2022-03-03 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0013_mapas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propuestas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.IntegerField(null=True)),
                ('centro', models.CharField(choices=[('Ninguna me convence', 'Ninguna me convence'), ('Bajar VT', 'Bajar VT'), ('Bajar PEEP', 'Bajar PEEP'), ('Bajar RR', 'Bajar RR')], max_length=25)),
            ],
        ),
    ]
