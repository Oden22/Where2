# Generated by Django 3.2.8 on 2021-10-24 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0003_auto_20211025_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='weather',
        ),
        migrations.AlterField(
            model_name='food',
            name='rating',
            field=models.FloatField(),
        ),
    ]
