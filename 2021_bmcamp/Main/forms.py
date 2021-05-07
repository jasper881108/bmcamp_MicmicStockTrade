from django import forms
from django.forms import ModelForm
from .models import TradeField


class trade_update(ModelForm):
    class Meta:
        model = TradeField
        fields = ['id','Company','TradePrice','ForSell']

class buy_update(ModelForm):
    class Meta:
        model = TradeField
        fields = ['id','Company','BuyPrice','ForBuy']