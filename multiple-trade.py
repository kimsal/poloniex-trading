import urllib3
urllib3.disable_warnings()
import poloniex
polo = poloniex.Poloniex('NTYJ7H1H-4Y6JLRUJ-QHSJDAN4-EQLLJ8FW','e279fd505fc334ac3fa7d2329f679f88ce10b04a1d936d59f59ac9d945a831d2c7a7e4315b2a7dccecf40647f110e85b07e1bf37988db20711526f80a5645d90', timeout=2)
#declare what coins you want to trade
play_coins = ['ETH',"ETC"]
balance = polo.api('returnCompleteBalances')
current_location = polo.api('returnTicker')
file_check = open("data_multi.csv","r")
data_check = file_check.read()
arr_data = data_check.split('\n')
index = 0
# Read old price data
def writeNewData(updated_data):
	f = open("data_multi.csv","w")
	f.write(str(updated_data))

file_note = open("note.txt","a")
file_help = open("count.txt",'a')
file_help.write("Executed\n")
help_store_old_data_from_file = ''
if (len(arr_data)-1) == len(play_coins):
	for coin in play_coins:
		help=0
		print coin + " current price: " + str(current_location['BTC_' + coin]['last'])
		current_btc_avaible = float(str(balance['BTC']['available']))
		current_coin_avaible = float(str(balance[coin]['available']))
		current_coin_order = float(str(balance[coin]['onOrders']))
		current_coin_price = float(str(current_location['BTC_'+coin]['last']))
		#btc info
		print "BTC avaible: " + str(current_btc_avaible)
		#lsk info
		print coin + " \tAvaible: " + str(current_coin_avaible)
		print "\tPrice: " + str(current_coin_price)
		print "\tOn Orders: " + str(current_coin_order)
		#Calculate amount to sell and buy
		number_to_sell = 1
		if current_coin_avaible <= 10:
			number_to_sell = current_coin_avaible
		elif current_coin_avaible <= 20:
			number_to_sell = current_coin_avaible/2
		else:
			number_to_sell = current_coin_avaible/3

		#kimsal Only
		if coin=="ETC":
			number_to_buy = 2
		else:
			number_to_buy = 1 

		try:
			if arr_data[index] == '':
				help = 1
				help_store_old_data_from_file + current_coin_price + '\n'
			old_price = float(arr_data[index])
			if float(str(balance['BTC']['available'])) > 0.00000001:
				print "You have some BTC: " + str(balance['BTC']['available']) + "BTC"
				#Trade LSK
				if (old_price-current_coin_price) >= (old_price*0.02):
					#Buy 1.15= 115%
					help = 1
					help_store_old_data_from_file =help_store_old_data_from_file + current_coin_price + '\n'
					print(polo.buy('BTC_' + coin, (current_coin_price - (old_price * 0.02)), number_to_buy))
					print "You Order " + coin + " " + str(number_to_buy)
					file_note.write("You Order " + coin + " " + str(number_to_buy))
				elif (current_coin_price - old_price) >= (old_price * 0.02):
					if current_coin_avaible > 0:
						#Sell
						help = 1
						help_store_old_data_from_file = help_store_old_data_from_file + current_coin_price + '\n'
						print(polo.sell('BTC_' + coin, (current_coin_price + (old_price*0.02)), number_to_sell))
						print "You sell " + coin + " " + str(number_to_sell)
						file_note.write("You sell " + coin + " " + str(number_to_sell))
				else:
					print "Can't buy or sell. " + coin + " old:"+str(old_price) + "BTC " + coin + " current  price:" + str(current_coin_price) + "BTC"
			else:
				print "You don't have any BTC"
				#sell LSK only
				if current_coin_avaible > 0:
						#0.44-0.40 >= (0.04)
					if (current_coin_price - old_price) >= (old_price * 0.02):
						#Sell
						help = 1
						help_store_old_data_from_file = help_store_old_data_from_file+ current_coin_price + '\n'
						print(polo.sell('BTC_' + coin, (current_coin_price + (old_price*0.02)), number_to_sell))
						print "You sell " + coin + " " + str(number_to_sell)
						file_note.write("You sell " + coin + " " + str(number_to_sell))
				else:
					print "No " + coin + " to sell."
			print "Price to buy:" + str((current_coin_price - (old_price * 0.02))) + "BTC"
			print 'price to sell:' + str((current_coin_price + (old_price * 0.02))) + "BTC"

		except Exception as e:
			print e.message
		if help == 0:
			help_store_old_data_from_file = help_store_old_data_from_file + str(arr_data[index]) + "\n"
		print "-----------End " + coin + "------------"
		index = index + 1
	print help_store_old_data_from_file
	writeNewData(help_store_old_data_from_file)
else:
	#write all data again because use might just remove or add some bitcoin to play (different length of play_coins)
	f = open("data_multi.csv","w")
	f.write("")
	for coin in play_coins:
		print coin + " current price: " + str(current_location['BTC_' + coin]['last'])
		current_btc_avaible = float(str(balance['BTC']['available']))
		current_coin_avaible = float(str(balance[coin]['available']))
		current_coin_order = float(str(balance[coin]['onOrders']))
		current_coin_price = float(str(current_location['BTC_'+coin]['last']))
		f = open("data_multi.csv","a")
		f.write(str(current_coin_price) + "\n")
	print "You just add or remove some coins to trade.So we added you location price plan"

