## FCN Pricing
# - Fixed coupon = Fixed rate of interest
# - Note = This product is packaged with bonds

## There are a few things I want to be clear:
## This FCN has a knock out & knock in barrier, but no call/ put parities 

''' 
FCN is also known as FCCN

FCCN = Fixed coupon callable note
FCN = Fixed coupon note

Aim: To achieve a risk return profile
character: Bond & equity (tied to underlying assets/ basket)
also pay interest to investors at regular intervals


We need the following variables:
1. Strike price (K)
2. Knock-out level (KO)/ call level - higher bound
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
df.index += 1 # Forces the index to start from `1`
# print(df.info(verbose = True))

# print(df.Date)

#Function works! 
# Function will find the next trading day that is returned in the dataframe
# def next_trade_date(start_date, add, df):
#     import pandas as pd
#     import datetime as datetime
#     end_date = pd.to_datetime(start_date) + datetime.timedelta(days = int(add))
#     if (end_date in list(df.Date)):
#         # print("YES")
#         return end_date
#     while (end_date not in list(df.Date)):
#         end_date += datetime.timedelta(days = int(add))
#     return end_date

#Both start and end trade dates will start here
def trade_date(df, given_date):
    import pandas as pd
    import datetime as datetime
    temp_date = pd.to_datetime(given_date)
    if temp_date in list(df.Date):
        return temp_date
    else:
        while (temp_date not in list(df.Date)):
            print(f"You cannot trade on {temp_date.date()} since it's a holiday", end = "\n\n")
            temp_date += datetime.timedelta(days = 1)
        return temp_date


def days_to_prorate (df, start = "2018-01-01", end = "2018-01-06"):
    import pandas as pd
    import datetime as datetime
    start, end = trade_date(df, start), trade_date(df, end)
    start_idx, end_idx = list(df.Date).index(start) + 1, list(df.Date).index(end) + 1
    print(f"Your first trade date is set to be {start.date()}")
    print(f"Your last trade date is set to be {end.date()}")
    if end_idx - start_idx > 0:
        return (end_idx - start_idx, start_idx, end_idx)
    else:
        return ValueError


# print(days_to_prorate(df, "2018-01-01", "2018-12-25"))


'''
Setting up our Pricing model

'''

# tenor period : months 
# strike = 95% of spot
# knock out, call level = 98% 
# Inital capital: 200k 

#No knock in barrier
def FCN_pricing (df, inital_spot, initial_date, period = 1, tenor = 6, coupon = 0.05, call = 0.98, strike = 0.95 ):
    initial_date = trade_date(df, initial_date).date()
    due_date = initial_date + datetime.timedelta(days = tenor * 30)
    # print(initial_date)
    due_date = trade_date(df, due_date).date()
    # print(due_date)
    prorate =  days_to_prorate(df, start = initial_date, end = due_date)[0]
    if period == 1:
        pass

print(FCN_pricing(df, 100, initial_date = "2021-01-01"))

for i in range (757, 883, (883-757)//6):
    print(i)

 