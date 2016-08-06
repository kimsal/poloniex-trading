#**An API wrapper for Poloniex.com written in Python**
#####poloniex.py - _Tested on Python 2.7.6 & 3.4.3_
Inspired by [this](http://pastebin.com/8fBVpjaj) wrapper written by 'oipminer'
##UPDATE!
> If you have been using an older version of python-poloniex wrapper you may need to generate new api keys. This is because (once again) the nonce has been 'optimized' (even more)! This is the last time, I swear...

###Features:
- ApiKey and Secret are optional if used for just public commands.
- Api Commands have been 'mapped' into methods for your conveniance.
- The `poloniex.Poloniex()` object has an optional 'timeout' attribute/arg that adjusts the number of seconds to wait for a response from polo (default = 3 sec)
- Optional api 'coach' can restrict the amount of calls per sec, keeping your api calls (that aren't threaded) under the limit (6 calls per sec). Activate the coach using `poloniex.Poloniex(coach=True)` when creating the polo object or by defining `polo._coaching = True`.
- We now build apon our _last_ 'nonce' instead of generating a new one everytime a private command is called! Nonces are now incemented by 1.
- Raises `ValueError` if the command supplied does not exist or if the api keys are not defined

##Install:
```bash
git clone https://github.com/s4w3d0ff/python-poloniex.git
cd python-poloniex

# Python 2
sudo python setup.py install
# Python 3
sudo python3 setup.py install
```
##Uninstall:
```bash
# Python 2
sudo pip uninstall poloniex
# Python 3
sudo pip3 uninstall poloniex
```
##Update:
```python
## Uninstall old ##
# Python 2
sudo pip uninstall poloniex
# Python 3
sudo pip3 uninstall poloniex

## Pull updates into cloned repo ##
cd python-poloniex
git pull

## Install update ##
# Python 2
sudo python setup.py install
# Python 3
sudo python3 setup.py install
```

##Useage:
#### **Basic Public Setup (no ApiKey/Secret):**
```python
import poloniex
polo = poloniex.Poloniex()
polo.timeout = 2
```
##### Get Ticker
```python
ticker = polo.api('returnTicker')
print(ticker['BTC_CGA'])
# or
ticker = polo.marketTicker()
print(ticker['BTC_CGA'])
```
##### Get Market Loan Orders
```python
BTCloanOrders = polo.api('returnLoanOrders',{'currency':'BTC'})
print(BTCloanOrders)
# or 
BTCloanOrders = polo.marketLoans('BTC')
print(BTCloanOrders)
```

#### **Basic Private Setup (ApiKey/Secret required):**
```python
import poloniex

polo = poloniex.Poloniex('yourApiKeyHere','yourSecretKeyHere123', timeout=1)
# or
polo.APIKey = 'yourApiKeyHere'
polo.Secret = 'yourSecretKeyHere123'
```
##### Get all your balances
```python
balance = polo.api('returnBalances')
print("I have %s CGA!" % balance['CGA'])
# or
balance = polo.myBalances()
print("I have %s BTC!" % balance['BTC'])
```
##### Make new CGA deposit address
```python
print(polo.api('generateNewAddress',{'currency':'CGA'}))
# or
print(polo.generateNewAddress('CGA'))
```
##### Sell 10 CGA for 0.003 BTC
```python
print(polo.api('sell', {'currencyPair': 'BTC_CGA', 'rate': '0.003' , 'amount': '10' }))
# or
print(polo.sell('BTC_CGA', '0.003', '10'))
```

**Examples of WAMP applications using the websocket push API can be found [here](https://github.com/s4w3d0ff/python-poloniex/tree/master/examples).**

You like?!
```
CGA: aZ1yHGx4nA64aWMDNQKXJrojso7gfQ1J5P
BTC: 15D8VaZco22GTLVrFMAehXyif6EGf8GMYV
LTC: LakbntAYrwpVSnLWj1fCLttVzpiDXDa5JV
DOGE: DAQjkQNbhpUoQw7KHAGkDYZ3yySKi751dd
```
#**Kimsal: More Not about how to run it:**
To run it:_
	Python multiple-trade.py
# note:
```
 if you want to play more coin or less coin, just add or remove it from variable named "play_coins"_
 # By default: play_coins = ['ETH',"ETC"]

  data_multiple.csv : is file to store old price of each coin.

  note.txt : is file to store note everytime you buy or sell coin.

  count.txt : is file to store note " How many time you executed the file. "