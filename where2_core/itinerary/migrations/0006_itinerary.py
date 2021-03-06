# Generated by Django 3.2.8 on 2021-10-25 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itinerary', '0005_food_time_scene'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activities', models.ManyToManyField(to='itinerary.Activity')),
                ('resturants', models.ManyToManyField(to='itinerary.Food')),
            ],
        ),
    ]
