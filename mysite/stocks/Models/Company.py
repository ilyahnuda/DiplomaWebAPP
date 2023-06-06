from django.db import models


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    weight = models.DecimalField(max_digits=12, decimal_places=4)
    price = models.DecimalField(max_digits=12, decimal_places=4)
    chg = models.DecimalField(max_digits=12, decimal_places=4)
    percent_chg = models.DecimalField(max_digits=12, decimal_places=4)
    founded = models.IntegerField()
    sector = models.CharField(max_length=100)
    sub_sector = models.CharField(max_length=200)

    def __str__(self):
        return self.name
