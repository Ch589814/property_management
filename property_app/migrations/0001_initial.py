# Generated by Django 5.1.2 on 2024-10-23 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('property_type', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('number_of_units', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_number', models.CharField(max_length=50)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('rent', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.property')),
            ],
        ),
        migrations.CreateModel(
            name='Lease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('rent_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.tenant')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property_app.unit')),
            ],
        ),
    ]
