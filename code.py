import conf      #imports conf.py fle stored in the same directory
import time
import json 
import requests
from boltiot import Bolt,Sms

bolt=Bolt(conf.BOLT_API,conf.DEVICE_ID)#we have configured our module connections
sms=Sms(conf.SSID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)# our twillio account is connected to our code

print("Whcih crypto are you interested in ")
print(" 1) BTC \n 2) ETH \n 3) BUSD \n 4) FIL \n 5) USDT ")

coin=str(input("Enter your choice: " )) #we take input of from the user

sell_price=float(input("Enter the  Sell price: ")) #input of sellin price
buy_price=float(input("Enter the Buy price: ")) #input of the buying price


# following is the function definition which will be called later
def price_check():
    url=("https://min-api.cryptocompare.com/data/price?fsym={}}&tsyms='USD'".format(coin.upper())) #coin.upper converts string into uppercase letters.
    response=requests.request("GET",url)
    response=json.loads(response.text)
    current_price=response['USD']
    return current_price


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


      except Exception as e:
           print(e)
      time.sleep(2) #introducing time delay 
      mybolt.digitalWrite("0","LOW") #off the buzzer 
      time.sleep(10)
