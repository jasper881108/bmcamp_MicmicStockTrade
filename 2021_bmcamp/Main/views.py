from django.shortcuts import render,redirect
from .forms import trade_update,buy_update
from .models import StockPrice,TradeField
from member.models import Account
from .task import clean_tradefield,update_stockprice
# Create your views here.


# query = str(TradeField.objects.all().query)
# df = pd.read_sql_query(query, connection)
#pd.DataFrame({'id':[1,2,3,4,5],'Company' : ['AAPL','AAPL','Google','Google','AAPL'],'ForSell':[True,False,True,False,True],'ForBuy':[False,True,False,True,False],'price':[10,10,20,20,15]})

def home_screen_view(request,*args,**kwargs):
    user = request.user
    context = {'companies':[]}
    name_li = list(set(StockPrice.objects.values_list('Company', flat=True)))
    for name in name_li:
        context['companies'].append({'name':name,'price':StockPrice.objects.filter(Company=name)[0]})

    if user.is_authenticated:

        if request.method == 'POST':
            form = trade_update(request.POST)
            if form.is_valid():
                account = Account.objects.get(username=user)
                company = form.cleaned_data.pop('Company')
                if getattr(account,company) > 0:
                    setattr(account, company, getattr(account, company) - 1)
                    new_form = form.save(commit=False)
                    new_form.User = user
                    new_form.save()
                    account.save()
                    context['no_enough_share'] = ''
                    return redirect('home')
                else:
                    context['no_enough_share'] = "You don't have any share to sell"
            form = buy_update(request.POST)
            if form.is_valid():
                company = form.cleaned_data.pop('Company')
                stock = StockPrice.objects.get(Company=company)
                if (stock.initial_share > 0) :
                    new_form = form.save(commit=False)
                    new_form.User = user
                    stock.initial_share -= 1
                    cost = form.cleaned_data.pop('BuyPrice')
                    account = Account.objects.get(username=user)
                    setattr(account,company,getattr(account, company) + 1)
                    account.money = account.money - cost
                    account.save()
                    stock.save()
                    return redirect('home')
                else:
                    new_form = form.save(commit=False)
                    new_form.User = user
                    cost = form.cleaned_data.pop('BuyPrice')
                    account = Account.objects.get(username=user)
                    account.money = account.money - cost
                    new_form.save()
                    account.save()
                    return redirect('home')
    else:
        context['not_login'] = 'Please Login or Register First'
    return render(request,'home_screen_view.html',context)

