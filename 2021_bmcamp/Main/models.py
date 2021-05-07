
# Create your models here.
from django.db import models
import time
import sys
# Create your models here.
class StockPrice(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='id')
    Company       = models.CharField(max_length=25,verbose_name='Company',default='Unknown')
    Times         = models.DateField(verbose_name='Times',default='Unknown')
    Price         = models.FloatField(verbose_name='Price',default=0.0)
    initial_share = models.PositiveIntegerField(verbose_name='initial',default=100)
    def __str__(self):
        return str(self.Price)
class StockPrice_History(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='id')
    Company       = models.CharField(max_length=25,verbose_name='Company',default='Unknown')
    Times         = models.DateField(verbose_name='Times',default='Unknown')
    Price         = models.FloatField(verbose_name='Price',default=0.0)

class TradeField(models.Model):
    id          = models.AutoField(primary_key=True,auto_created=True,serialize=False, verbose_name='id')
    User        = models.CharField(max_length=50, verbose_name='User',default='Unknown')
    Company     = models.CharField(max_length=25, verbose_name='Company',default='Unknown')
    TradePrice  = models.FloatField(verbose_name='TradePrice',default=0.0)
    TradeTime   = models.DateField(auto_now_add=True,verbose_name='TradeTime')
    ForSell     = models.BooleanField(default=False,verbose_name='ForSell')
    ForBuy      = models.BooleanField(default=False,verbose_name='ForBuy')
    BuyPrice    = models.FloatField(verbose_name='BuyPrice',default=0.0)
