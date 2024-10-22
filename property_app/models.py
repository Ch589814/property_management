from django.db import models

# Create your models here.

from django.db import models

class Property(models.Model):
    PROPERTY_TYPES = [
        ('Apartment', 'Apartment'),
        ('House', 'House'),
        ('Commercial', 'Commercial'),
    ]
    name = models.CharField(max_length=100)
    address = models.TextField()
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    description = models.TextField()
    number_of_units = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Unit(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    unit_number = models.CharField(max_length=10)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    rent = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Unit {self.unit_number} - {self.property.name}"

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Lease(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='leases')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='leases')
    start_date = models.DateField()
    end_date = models.DateField()
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Lease: {self.tenant.name} - {self.unit.unit_number}"

