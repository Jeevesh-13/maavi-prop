# Generated by Django 3.0.6 on 2020-06-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0002_auto_20200524_1532'),
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.CharField(max_length=30)),
                ('station_id', models.CharField(max_length=30)),
                ('stop_number', models.IntegerField()),
                ('arrival_time', models.TimeField()),
                ('departure_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_id', models.CharField(max_length=30)),
                ('station_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.CharField(max_length=30)),
                ('train_name', models.CharField(max_length=30)),
                ('train_type', models.CharField(max_length=30)),
                ('source_id', models.CharField(max_length=30)),
                ('destination_id', models.CharField(max_length=30)),
            ],
        ),
    ]
