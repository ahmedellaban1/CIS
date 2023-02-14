from django.db import models

from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class City(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    city_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.city_name


class CityDistrict(models.Model):
    district = models.CharField(max_length=50)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.city)+' - '+str(self.district)


class Job(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return f"{self.id} {self.name}"