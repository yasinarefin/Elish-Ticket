from django.db import models

# Create your models here.
class BusStructure(models.Model):
    BusModel = models.CharField(max_length=20, default=None, null=False)
    HasAc = models.BooleanField(null=False)
    seatStructure = models.JSONField()

    def __str__(self):
        return "%s" % (self.BusModel)  # return Name of the Bus model on query


class Bus(models.Model):
    BusNumber = models.CharField(max_length=10, default=None, null=False)
    CoachNo = models.CharField(max_length=10, default=None, null=True)
    Active = models.BooleanField(default=True, null=False)
    Price = models.DecimalField(
        max_digits=5, decimal_places=2, default=None, null=False
    )
    BusStructure = models.ForeignKey(BusStructure, on_delete=models.CASCADE)


class Schedule(models.Model):
    Day = models.CharField(max_length=10, default=None, null=False)
    ArrivalPoint_and_time = models.JSONField()
    DepurturePoint_and_time = models.JSONField()
    BusSchedule = models.ManyToManyField(Bus, through="BusSchedule")


class BusSchedule(models.Model):
    Bus = models.ForeignKey(Bus, on_delete=models.CASCADE)
    Schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    StartCity = models.CharField(max_length=20, default=None, null=False)
    EndCity = models.CharField(max_length=20, default=None, null=False)
