# Generated by Django 4.0.3 on 2022-03-11 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCI_App', '0042_delete_mapas_alter_like_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='value',
            field=models.CharField(choices=[('Like', 'Like'), ('Unlike', 'Unlike')], default='Like', max_length=15),
        ),
    ]
