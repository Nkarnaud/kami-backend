import math

from django.db import models

# Create your models here.


class Airplane(models.Model):
    name = models.CharField(max_length=100)
    plane_id = models.IntegerField(default=0, unique=True)
    number_of_seats = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        unique_together = ('name', 'plane_id')

    @property
    def fuel_capacity(self):
        return 200 * self.id

    @property
    def fuel_consumption(self):
        return math.log(self.id) * 0.80

    @property
    def total_consumption(self):
        return self.base_fuel_consumption + (self.passengers * 0.002)

    @property
    def flight_duration(self):
        if self.total_fuel_consumption > 0:
            return self.fuel_capacity / self.total_consumption
        return 0
