# Cryptocurrency_Alert_system

This is very basic project which alerts you when the crypto price varies.
It alerts you when market price of the crypto you want to invest into varies more or less then you selling and buying price.

The code is very simple to understand.

# Code explanation 
We stat by importing the important libraries into our code 
Then we pass API's and Device ID to our Bolt and Sms
bolt=Bolt(conf.BOLT_API,conf.DEVICE_ID) #we have configured our module connections
sms=Sms(conf.SSID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)# our twillio account is connected to our code


# Following is the function definition which will be called later
```
def price_check():
    url=("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms={}".format(currency.upper()))#currency.upper converts string into uppercase letters.
    response=requests.request("GET",url)
    response=json.loads(response.text)
    current_price=response[currency.upper()]
    return current_price
```
    
    
#Main logic of the code 
```
   while True:
       market_price=price_check()
       print("Market price: ",market_price)
       try:
           if market_price<buy_price:
              mybolt.digitalWrite("0","HIGH")  #if market price is more then our selling price then buzzer starts beeping
              response1=sms.send_sms("\nMarket value has just hit your Buying price ") #Twilio sends SMS to our phone
              print("Status of SMS "+str(response1.status)) 

           elif market_price>sell_price:
              print("\nMarket Price is more then your selling price\n ")
              mybolt.digitalWrite('0','HIGH')   #if market price is more then our selling price then buzzer starts beeping 
              response1=sms.send_sms("Market price has just crossed your selling price ")
              print("Status of SMS "+str(response1.status)) # twilio send message your number 
```              
              
#Remember try will not work without execpt 
so we write execpt and then in the end we introduce time dalay by using time.sleep()
```
except Exception as e:
           print(e)
      time.sleep(2) #introducing time delay 
      mybolt.digitalWrite("0","LOW") #off the buzzer 
      time.sleep(10)
```



