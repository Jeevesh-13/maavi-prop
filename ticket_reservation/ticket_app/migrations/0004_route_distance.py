# Generated by Django 3.0.6 on 2020-06-02 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0003_route_station_train'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='distance',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
