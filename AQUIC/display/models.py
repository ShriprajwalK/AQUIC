from django.db import models
from  django.utils import timezone

class Value(models.Model):
    id_no = models.IntegerField()
    check = models.IntegerField(default=0)
    temp = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    lpg = models.FloatField(default=0)
    propane = models.FloatField(default=0)
    carbon_monoxide = models.FloatField(default=0)
    carbon_dioxide = models.FloatField(default=0)
    ammonia =  models.FloatField(default=0)
    methane =  models.FloatField(default=0)
    alcohol =  models.FloatField(default=0)
    smoke =  models.FloatField(default=0)
    dust =  models.FloatField(default=0)
    date_time = models.DateTimeField(default = timezone.now)

    def update(self):
        self.save()

    def __str__(self):
        return str(self.date_time) + "_" + str(self.id_no)
