from django.db import models


class Coin(models.Model):
    rank = models.IntegerField(blank=True, null=True)
    logo = models.URLField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    market_cap = models.FloatField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
