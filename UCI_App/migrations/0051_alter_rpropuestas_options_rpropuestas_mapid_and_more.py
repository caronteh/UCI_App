# Generated by Django 4.0.3 on 2022-03-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0050_delete_propuestas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rpropuestas',
            options={'verbose_name': 'Propuesta', 'verbose_name_plural': 'Propuestas'},
        ),
        migrations.AddField(
            model_name='rpropuestas',
            name='MapID',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rpropuestas',
            name='value',
            field=models.CharField(default='No me convence', max_length=25),
        ),
    ]
