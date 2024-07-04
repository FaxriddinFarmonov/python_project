from django.db import models

# Create your models here.
from django.db import models
class Book(models.Model):
    name = models.CharField(max_length=15)

    def __str__(self):
        return self.name


from django.db import models

class Load(models.Model):
    name = models.CharField(max_length=255, null=True)
    published_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    pickup_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    dlv_date = models.DateField(null=True, blank=True)
    to_dlv_date = models.DateField(null=True, blank=True)
    origin = models.CharField(max_length=255)
    dh_o = models.FloatField(null=True)
    destination = models.CharField(max_length=255, null=True)
    dh_d = models.FloatField(null=True)
    distance = models.FloatField(null=True)
    length = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    suggested_price = models.FloatField(null=True, blank=True)
    commodity = models.CharField(max_length=255, null=True)
    contact = models.CharField(max_length=100, null=True)
    contact_type = models.CharField(max_length=20, null=True)
    comment = models.CharField(max_length=120, null=True)
    ref_number = models.CharField(max_length=120, null=True)
    truck_status_choices = [
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered')
    ]
    truck_status = models.CharField(max_length=10, choices=truck_status_choices, null=True, blank=True)
    results_count = models.IntegerField(null=True, blank=True, default=0)
    results_data = models.JSONField(null=True, blank=True)




