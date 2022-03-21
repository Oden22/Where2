from django.db import models
from django.db.models.fields.related import ForeignKey

weather_choices = [
    ('SU', 'Sunny'),
    ('RA', 'Raining')
]

cost_choices = [
    ('HI', 'High'),
    ('ME', 'Medium'),
    ('LO', 'Low'),
    ('FR', 'Free')
]

time_choices = [
    ('BR', 'Breakfast'),
    ('LU', 'Lunch'),
    ('DI', 'Dinner'),
]

genre_choices = [
    ('AC', 'Activity'),
    ('FO', 'Food')
]

class Activity(models.Model):
    #Activities model.
    genre = models.CharField(max_length=2, choices=genre_choices)
    title = models.CharField(max_length=64)
    weather = models.CharField(max_length=2, choices=weather_choices)

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    description = models.TextField(max_length=1024)
    cost = models.CharField(max_length=2, choices=cost_choices)

    def __str__(self):
        return self.title + " " + self.weather

class Resturant(models.Model):
    #Resturant Model
    genre = models.CharField(max_length=2, choices=genre_choices)
    title = models.CharField(max_length=64)

    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    description = models.TextField(max_length=1024)
    cost = models.CharField(max_length=2, choices=cost_choices)
    rating = models.FloatField()
    time_scene = models.CharField(max_length=2, choices=time_choices)

    def __str__(self):
        return self.title + ' ' + self.time_scene
