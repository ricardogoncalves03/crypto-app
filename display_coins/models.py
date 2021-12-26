from django.db import models

class Coin(models.Model):
    rank = models.IntegerField()
    logo = models.URLField()
    name = models.CharField(max_length=200)
    price = models.FloatField()
    market_cap = models.FloatField(max_length=200)
    
    def __str__(self):
        return self.name