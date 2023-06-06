from django.contrib import admin

# Register your models here.
from .Models.Company import Company
from .Models.News import News
from .Models.StockIndex import StockIndex

admin.site.register(Company)
admin.site.register(News)
admin.site.register(StockIndex)
