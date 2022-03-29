# Generated by Django 4.0.3 on 2022-03-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0024_remove_mapas_paciente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapas',
            name='Centro',
            field=models.CharField(choices=[('JX', 'JX'), ('VH', 'VH')], max_length=15, verbose_name='Centro'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='Habitacion',
            field=models.CharField(choices=[('BOX01', 'BOX01'), ('BOX02', 'BOX02')], max_length=15, verbose_name='Habitacion'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='ID',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='MP',
            field=models.FloatField(null=True, verbose_name='MP'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='PEEP',
            field=models.FloatField(null=True, verbose_name='PEEP'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='PPeak',
            field=models.FloatField(null=True, verbose_name='PPeak'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='PPlato',
            field=models.FloatField(null=True, verbose_name='PPlato'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='RR',
            field=models.FloatField(null=True, verbose_name='RR'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='Servicio',
            field=models.CharField(choices=[('UCI1', 'UCI1'), ('UCI2', 'UCI2'), ('UCIA', 'UCIA'), ('UCIP', 'UCIP'), ('UCIN', 'UCIN')], max_length=15, verbose_name='Servicio'),
        ),
        migrations.AlterField(
            model_name='mapas',
            name='VT',
            field=models.FloatField(null=True, verbose_name='VT'),
        ),
    ]