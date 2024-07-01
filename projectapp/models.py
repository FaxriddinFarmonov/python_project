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





# models.py

# from django.db import models
#
# class Load(models.Model):
#     pickup_city_state = models.CharField(max_length=255)
#     delivery_city_state = models.CharField(max_length=255)
#     pickup_date = models.DateField()
#     length = models.CharField(max_length=10)
#     weight = models.CharField(max_length=10)
#     delivery_date = models.DateField()
#     reference_load_number = models.CharField(max_length=255)
#     commodity = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     type = models.CharField(max_length=50, default='Dry Van')
#     ftl_ltl = models.CharField(max_length=3, default='FTL')  # FTL or LTL
#     name = models.CharField(max_length=255)
#     contact = models.CharField(max_length=255)  # Store email or phone
#     load_description = models.TextField()
#
#     def __str__(self):
#         return f"Load {self.id}"
#
