from django.db import models


class StockIndex(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=False)
    open_val = models.DecimalField(max_digits=12, decimal_places=4)
    high_val = models.DecimalField(max_digits=12, decimal_places=4)
    low_val = models.DecimalField(max_digits=12, decimal_places=4)
    close_val = models.DecimalField(max_digits=12, decimal_places=4)
    adjclose_val = models.DecimalField(max_digits=12, decimal_places=4)
    volume_val = models.IntegerField()
    symbol = models.ForeignKey('Company', on_delete=models.PROTECT, null=False)
