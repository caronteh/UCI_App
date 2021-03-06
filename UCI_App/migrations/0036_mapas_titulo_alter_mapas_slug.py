# Generated by Django 4.0.3 on 2022-03-10 18:14

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0035_alter_mapas_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapas',
            name='titulo',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='titulo'),
        ),
    ]
