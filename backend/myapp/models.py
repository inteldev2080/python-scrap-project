from django.db import models


class CryptoModel(models.Model):
    name = models.CharField(max_length=250) 
    price = models.DecimalField(max_digits=18, decimal_places=10)
    perhour = models.DecimalField(max_digits=4, decimal_places=2)
    day = models.DecimalField(max_digits=4, decimal_places=2)
    week = models.DecimalField(max_digits=4, decimal_places=2)
    marketcap = models.DecimalField(max_digits=12, decimal_places=0)
    volume = models.DecimalField(max_digits=12, decimal_places=0)
    cirulating_supply = models.CharField(max_length=250)

    def __str__(self):
        return self.name