from django.contrib.auth.models import User
from django.db import models


class ClubUsers(models.Model):
    f_name = models.CharField('First Name', max_length=30)
    l_name = models.CharField('Last name', max_length=30)
    email_address = models.EmailField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=25, blank=True)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Venue(models.Model):
    name = models.CharField('Name of Venue', max_length=30)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15, blank=True)
    phone_number = models.CharField(max_length=25, blank=True)
    web_address = models.URLField(max_length=50, blank=True)
    email_address = models.EmailField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=30)
    event_date = models.DateField()
    event_time = models.TimeField()
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    attendees = models.ManyToManyField(ClubUsers)

    def __str__(self):
        return self.name
