## FCN Pricing
# - Fixed coupon = Fixed rate of interest
# - Note = This product is packaged with bonds

''' 
FCN is also known as FCCN

FCCN = Fixed coupon callable note
FCN = Fixed coupon note

Aim: To achieve a risk return profile
character: Bond & equity (tied to underlying assets/ basket)
also pay interest to investors at regular intervals


We need the following variables:
1. Strike price (K)
2. Knock-out level (KO) - higher bound
3. Knock-in level (KI) - lower bound = for soft protection
4. Maturity date = contract comes to an end
5. Observation interval = coupon/ interest pay out date

Conditions:
- if worst performing asset touches KO, everything expires IMMEDIATELY & pay out
- if any asset touches KI, pay  out gets decided by worst performing asset



Fake scenario:
- Basket portoflio contains: ETC, Bitcoin
- Expiary = 28 days 

'''

import matplotlib.pyplot as plt
import yfinance as yf

tickers_list = 'AAPL, MSFT'
tickers_info = yf.Tickers(tickers_list)
data = yf.download(tickers_list, start = "2018-01-01",end = "2022-01-01")
print(data["Close"])

def FCN (tenor):
    pass