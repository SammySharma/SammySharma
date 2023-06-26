#Market_wizard_bot
from dhanhq import dhanhq
import pandas as pd
import time
import json
#Creds

dhan = dhanhq("<client ID>","<API ACCESS CODE>")

#SYMBOL_DATA
stocks = []
df = pd.DataFrame()
while True:
    symbol = str(input("Please Enter Symbols to Watch : "))
    stocks.append(symbol)
    done = str(input("Please type done once your list is complete : "))
    if done == "done":
        break


for symbol in stocks:
    stocks_data = dhan.historical_minute_charts(
                symbol=symbol,
                exchange_segment='NSE_EQ',
                instrument_type='EQUITY',
                expiry_code=0,
                from_date='2023-06-01',
                to_date='2023-06-23'
                )
    stock_df = pd.DataFrame(stocks_data['data'])
    stock_df.columns = ['OPEN', 'HIGH', 'LOW', 'CLOSE', 'VOLUME', 'START_TIME']
    stock_df['START_TIME'] = pd.to_datetime(stock_df['START_TIME'], unit='s').dt.date
    stock_df.insert(0, 'STOCK', symbol)
    df = pd.concat([df, stock_df])

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)

# Display the DataFrame
print(df)
    



