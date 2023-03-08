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
6. fixed-coupon-rate = 
    - e.g. if pa is 20%, quarterly is 5% flat coupon

Conditions:
- if worst performing asset touches KO, everything expires IMMEDIATELY & pay out
- if any asset touches KI, pay  out gets decided by worst performing asset



Fake scenario:
- Basket portoflio contains: ETC, Bitcoin
- Expiary = 28 days 

'''

import matplotlib.pyplot as plt     #For plotting
import yfinance as yf   #Importing yahoo finance stock data
import pandas as pd
import datetime as datetime

tickers_list = 'AAPL, MSFT'
tickers_info = yf.Tickers(tickers_list)

start_interval = "2018-01-01"
end_interval = "2022-01-01"
data = yf.download(tickers_list, start = start_interval,end = end_interval)

df = data["Close"]
df.reset_index(inplace = True)
# print(df.info(verbose = True))


#Function works! 
# Function will find the next trading day that is returned in the dataframe
def next_trade_date(start_date, add, df):
    import pandas as pd
    import datetime as datetime
    end_date = pd.to_datetime(start_date) + datetime.timedelta(days = int(add))
    if (end_date in list(df.Date)):
        # print("YES")
        return end_date
    while (end_date not in list(df.Date)):
        end_date += datetime.timedelta(days = int(add))
    return end_date

print(df.Date)
print(next_trade_date("2018-01-05", 1, df))
