from background_task import background
import pandas as pd
from .models import TradeField,StockPrice,StockPrice_History
from member.models import Account
import random
import time
@background()
def clean_tradefield():
    df = pd.DataFrame(
        list(TradeField.objects.values('id', 'User', 'Company', 'ForSell', 'ForBuy', 'TradePrice', 'BuyPrice')))
    df['price'] = df.TradePrice + df.BuyPrice
    idx = 0
    l_sell = []
    l_buy = []
    k = df.groupby(['Company', 'price']).agg(
        {'ForSell': lambda x: x.sum().max(), 'ForBuy': lambda x: x.sum().max()}).min(1)
    for group in df.groupby(['Company', 'price']):
        l_sell.append(group[-1].loc[df['ForSell'] == True].sample(int(k[idx])))
        l_buy.append(group[-1].loc[df['ForBuy'] == True].sample(int(k[idx])))
        idx += 1
    sell_order = pd.concat(l_sell)
    buy_order = pd.concat(l_buy)

    for id in sell_order.id.tolist():
        obj = df[df['id'] == id]
        account = Account.objects.get(username=str(obj['User'].values[0]))
        account.money += obj['price'].values[0]
        account.save()

    for id in buy_order.id.tolist():
        obj = df[df['id'] == id]
        account = Account.objects.get(username=str(obj['User'].values[0]))
        account.money -= obj['price'].values[0]
        account.save()

    sell_delete = TradeField.objects.filter(id__in=sell_order.id.tolist())
    sell_delete.delete()
    buy_delete = TradeField.objects.filter(id__in=buy_order.id.tolist())
    buy_delete.delete()

@background()
def update_stockprice():
    now = time.time()
    if (round(now - 1620406927.024472,0) % 5) == 0 :
        df = pd.DataFrame(
            list(StockPrice.objects.values('Company', 'Price')))
        for company in df.Company.tolist():
            obj = df[df['Company'] == company]
            stock = StockPrice.objects.get(Company=company)
            stock.Price = round(obj['Price'].values[0] * (1+random.randrange(-70,70,1)/100),2)
            stock.save()