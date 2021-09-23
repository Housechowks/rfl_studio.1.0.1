from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import BLANK_CHOICE_DASH
from Products.models import Truck
#from profiles.models import profile
from django.utils import timezone
#from .utills import generate_code

#position is an instance of a single transaction

class Position(models.Model):
    Product = models.ForeignKey(Truck, on_delete=CASCADE)
    Delivery_Number = models.CharField(blank=BLANK_CHOICE_DASH, max_length=10)
    current_rates =models.IntegerField(blank= True)
    destination = models.SmallIntegerField(help_text='K ', default= 1)
    tonnages = models.FloatField(help_text= ' tons ')
    
    created = models.DateField(blank=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.Product.tonnages * self.current_rates
        return super().save(*args, **kwargs)

    def __str__(self):
        return f" id: {self.id}, TRUCK: {self.Product.plate_number}, TONNAGES:{self.tonnages},DESTINATION K:{self.destination}"


