from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=200)
    latlong = models.CharField(max_length=40)
    initials = models.CharField(max_length=2)

    def __str__(self):
        return self.name


class Postcard(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    sent = models.DateField()
    received = models.DateField()
    distance = models.CharField(max_length=40)
    time_travel = models.CharField(max_length=4)
    image = models.ImageField(upload_to="uploads/", blank=True)

    def __str__(self):
        return str(self.received)
