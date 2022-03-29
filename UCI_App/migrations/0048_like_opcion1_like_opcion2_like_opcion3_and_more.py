# Generated by Django 4.0.3 on 2022-03-13 17:45

import autoslug.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('UCI_App', '0047_alter_mapeo_centros'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='Opcion1',
            field=models.CharField(choices=[('No me convence', 'No me convence'), ('Bajar VT', 'Bajar VT')], default='No me convence', max_length=15),
        ),
        migrations.AddField(
            model_name='like',
            name='Opcion2',
            field=models.CharField(choices=[('No me convence', 'No me convence'), ('Bajar PEEP', 'Bajer PEEP')], default='No me convence', max_length=15),
        ),
        migrations.AddField(
            model_name='like',
            name='Opcion3',
            field=models.CharField(choices=[('No me convence', 'No me convence'), ('Bajar RR', 'Bajar RR')], default='No me convence', max_length=15),
        ),
        migrations.AddField(
            model_name='mapeo',
            name='PEEPBajado',
            field=models.ManyToManyField(blank=True, default=None, related_name='PEEPBajado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mapeo',
            name='RRBajado',
            field=models.ManyToManyField(blank=True, default=None, related_name='RRBajado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='mapeo',
            name='VTBajado',
            field=models.ManyToManyField(blank=True, default=None, related_name='VTBajado', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mapeo',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=False, populate_from='NumID'),
        ),
    ]