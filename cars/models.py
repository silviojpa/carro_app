from django.db import models

# Create your models here.

class Brand(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car (models.Model):
    ID = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200,)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') # brand = marca
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self): #São padróes em model 
        return self.model # Traz o nome do dentro do model 


class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'