from typing import DefaultDict
from django.db import models
from django.db.models.fields import BLANK_CHOICE_DASH



class Truck(models.Model):
    Contract_spec = models.CharField(max_length=10, blank=True)
    plate_number = models.CharField(max_length=10)
    Delivery_Number = models.CharField(blank=BLANK_CHOICE_DASH, max_length=10)
    destination = models.SmallIntegerField(help_text='K ', default= 1)
    current_rates =models.IntegerField(blank= True)
    material_spec = models.CharField(max_length=10, blank=True)
    tonnages = models.FloatField(help_text= ' tons ')
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)



    def __str__(self):
        return f"{self.plate_number}-{self.created.strftime('%d/%m/%y')}"

