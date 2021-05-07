# bmcamp_MicmicStockTrade

### The website create for NSYSU 2021 BM camp, notice that every stock here is FAKE!!

<br>
<br>
<br>
<br>

# Structure

### Backend             -     Django
### DataVisiualize      -     Plotly & Dash
### DataBase            -     Sqlite3(Django built-in DB)

# Product demo

<br>
<br>

### Main page
![Main page](/images/Main_page.png)
![Main page2](/images/Main_page2.png)
![Main page3](/images/Main_page3.png)

<br>
<br>
<br>
<br>


# Intro

<br>
<br>

### Create SuperUser by typing [ python manage.py createsuperuser ]. 
### After going into the directory, use [ python manage.py runserver ] at terminal to run the whole project
### Finally, Typing [ python manage.py process_tasks ] to run background code 

<br>
<br>
<br>
<br>

# Models explain

<br>
<br>

### Account 
![Admin_account](/images/Admin_account.png)
Place With Email, username, passward, shares, money holded.

<br>
<br>

### TradeField
![Admin_tradefield](/images/Admin_tradefield.png)
Place recording every trade decision made by individuals. Including selling-price and purchasing-price, buyer's and seller's id, Company etc.

<br>
<br>

### StockPrice
![Admin_stockprice](/images/Admin_stockprice.png)
Place to trace the current stock price of every single stock and the remaining free shares it has.








