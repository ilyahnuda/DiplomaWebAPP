from django.db import models
from ..Models.Index import Index


class HistoricalDataIndex(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(null=False)
    open_val = models.DecimalField(max_digits=12, decimal_places=4)
    high_val = models.DecimalField(max_digits=12, decimal_places=4)
    low_val = models.DecimalField(max_digits=12, decimal_places=4)
    close_val = models.DecimalField(max_digits=12, decimal_places=4)
    adjclose_val = models.DecimalField(max_digits=12, decimal_places=4)
    volume_val = models.BigIntegerField()
    financeindex = models.ForeignKey('Index', on_delete=models.PROTECT, null=False)
