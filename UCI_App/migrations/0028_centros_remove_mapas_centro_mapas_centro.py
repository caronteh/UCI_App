# Generated by Django 4.0.3 on 2022-03-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0027_mapas_propuestas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Centros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Centro', models.CharField(max_length=15, verbose_name='Centro')),
            ],
        ),
        migrations.RemoveField(
            model_name='mapas',
            name='Centro',
        ),
        migrations.AddField(
            model_name='mapas',
            name='Centro',
            field=models.ManyToManyField(to='UCI_App.centros'),
        ),
    ]
