from django.db import models
from datetime import datetime
from django.utils import timezone

class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Post(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    @property
    def post_age(self):
        age = timezone.now() - self.created_at 
        return int(age.days)
    

class ToyManager(models.Manager):
    def get_animals(self):
        return self.filter(category='animals')

    def get_vehicles(self):
        return self.filter(category='vehicles')

    def get_robots(self):
        return self.filter(category='robots')

    def get_red_toys(self):
        return self.filter(color='red')

    def get_sound_making_animals(self):
        return self.filter(category='animals', makes_sound=True)

class Toy(models.Model):
    CATEGORY_CHOICES = [
        ('animals', 'Animals'),
        ('vehicles', 'Vehicles'),
        ('robots', 'Robots'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=10)
    makes_sound = models.BooleanField()

    objects = ToyManager()

    def __str__(self):
        return self.name
