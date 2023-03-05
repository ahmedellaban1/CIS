from django.db import models
from django.contrib.auth.models import User
from accounts.models import HerafiInformation, City, CityDistrict  # type: ignore
from main_info.models import Job  # type: ignore

# Create your models here.
day_list = (
            ('sunday', 'sunday'),
            ('monday', 'monday'),
            ('tuesday', 'tuesday'),
            ('wednesday', 'wednesday'),
            ('thursday', 'thursday'),
            ('friday', 'friday'),
            ('saturday', 'saturday')
)
ticket_status = (
            ('pending', 'pending'),
            ('done', 'done'),
            ('expired', 'expired'),
            ('been refused', 'been refused'),
            ('been accepted', 'been accepted'),

)


class Schedule(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    date = models.DateField()
    day = models.CharField(choices=day_list, max_length=10)
    time = models.TimeField()
    herafi_id = models.ForeignKey(HerafiInformation, on_delete=models.CASCADE)


class Ticket(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    date= models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    client_id = models.ForeignKey(User, on_delete=models.CASCADE)
    evaluation = models.FloatField(null=True, blank=True)
    comment = models.TextField(max_length=1000, null=True, blank=True)
    status = models.CharField(max_length=13, choices=ticket_status, default=ticket_status[0][0], null=True, blank=True)
    description = models.TextField(max_length=2000, help_text="describe your problem ")
    job_category_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    city_district = models.ForeignKey(CityDistrict, on_delete=models.DO_NOTHING)
    herafi = models.ForeignKey(HerafiInformation, on_delete=models.CASCADE)
