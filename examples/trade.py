import urllib3
urllib3.disable_warnings()
import poloniex

polo = poloniex.Poloniex('NTYJ7H1H-4Y6JLRUJ-QHSJDAN4-EQLLJ8FW','e279fd505fc334ac3fa7d2329f679f88ce10b04a1d936d59f59ac9d945a831d2c7a7e4315b2a7dccecf40647f110e85b07e1bf37988db20711526f80a5645d90', timeout=2)
balance = polo.api('returnCompleteBalances')
current_location = polo.api('returnTicker')
print "LSK current price: " +str(current_location['BTC_LSK']['last'])
current_btc_avaible = float(str(balance['BTC']['available']))
current_lsk_avaible = float(str(balance['LSK']['available']))
current_lsk_order = float(str(balance['LSK']['onOrders']))
current_lsk_price = float(str(current_location['BTC_LSK']['last']))
#btc info
print "BTC avaible: "+str(current_btc_avaible)
#lsk info
print "LSK \tAvaible: "+str(current_lsk_avaible)
print "\tPrice: "+str(current_lsk_price)
print "\tOn Orders: "+str(current_lsk_order)
#Calculate amount to sell and buy
number_to_sell=1
if current_lsk_avaible<=10:
	number_to_sell=current_lsk_avaible
elif current_lsk_avaible<=20:
	number_to_sell=current_lsk_avaible/2
else:
	number_to_sell=current_lsk_avaible/3

number_to_buy=10

# Read old price data
def writeNewData():
	f=open("data.csv","w")
	f.write(str(current_lsk_price))
try:
	file=open("data.csv","r")
	data=file.read()
	if data=='':
		writeNewData()
	old_price=float(data)
	if float(str(balance['BTC']['available']))>0.00000001:
		print "You have some BTC: "+str(balance['BTC']['available'])+"BTC"
		#Trade LSK
		if (old_price-current_lsk_price)>=(old_price*0.07):
			#Buy 1.15= 115%
			writeNewData()
			print(polo.buy('BTC_LSK', (current_lsk_price-(old_price*0.07)), number_to_buy))
		elif (current_lsk_price-old_price)>=(old_price*0.07):
			if current_lsk_avaible>0:
				#Sell
				writeNewData()
				print(polo.sell('BTC_LSK', (current_lsk_price+(old_price*0.07)), number_to_sell))
		else:
			print "Can't buy or sell. LSK old:"+str(old_price)+",LSK current  price:"+str(current_lsk_price)
	else:
		print "You don't have any BTC"
		#sell LSK only
		if current_lsk_avaible>0:
				#0.44-0.40 >= (0.04)
			if (current_lsk_price-old_price)>=(old_price*0.07):
				#Sell
				writeNewData()
				print(polo.sell('BTC_LSK', (current_lsk_price+(old_price*0.07)), number_to_sell))
		else:
			print "No LSK to sell."
	print "Price to buy:"+str((current_lsk_price-(old_price*0.07)))
	print 'price to sell:'+str((current_lsk_price+(old_price*0.07)))
except Exception as e:
	print e.message