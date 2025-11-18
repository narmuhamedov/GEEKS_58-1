from django.db import models

class Car(models.Model):
    name_car = models.CharField(max_length=100)

    def __str__(self):
        return self.name_car


class CarNumber(models.Model):
    number_car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='cars')
    number = models.CharField(max_length=100, default='KG')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.number_car}-{self.number}'
    

