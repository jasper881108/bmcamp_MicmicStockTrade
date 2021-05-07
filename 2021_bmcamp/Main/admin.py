from django.contrib import admin
from .models import StockPrice,TradeField
# Register your models here.
class StockPriceAdmin(admin.ModelAdmin):
    list_display = ('id',  'Company', 'Times', 'Price','initial_share')
    search_fields = ('id', 'Company', 'Price')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(StockPrice,StockPriceAdmin)

class TradeFieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'User', 'Company', 'TradePrice', 'TradeTime', 'ForSell','ForBuy','BuyPrice')
    search_fields = ('User', 'Company', 'TradePrice','BuyPrice')
    readonly_fields = ('id', 'Company', 'TradePrice','BuyPrice')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(TradeField,TradeFieldAdmin)