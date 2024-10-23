from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50)
    description = models.TextField()
    number_of_units = models.IntegerField()

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    unit_number = models.CharField(max_length=20)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)




