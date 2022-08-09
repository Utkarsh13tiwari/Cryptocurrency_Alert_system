# Cryptocurrency_Alert_system

This is very basic project which alerts you when the crypto price varies.
It alerts you when market price of the crypto you want to invest into varies more or less then you selling and buying price.

The code is very simple to understand.

# Code explanation 
We stat by importing the important libraries into our code 
Then we pass API's and Device ID to our Bolt 
bolt=Bolt(conf.BOLT_API,conf.DEVICE_ID) #we have configured our module connections

# following is the function definition which will be called later
def price_check():
    url=("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={}".format(currency.upper()))#currency.upper converts string into uppercase letters.
    response=requests.request("GET",url)
    response=json.loads(response.text)
    current_price=response[currency.upper()]
    return current_price
    

