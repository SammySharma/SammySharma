#Market_wizard_bot
from dhanhq import dhanhq
import pandas as pd
import time
import pytz
#Creds

dhan = dhanhq("<CLIENT_ID>","<Access_key>")

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
    
    #Convert Start_time in Date
    temp_list = []
    for i in stock_df['START_TIME']:
        temp = dhan.convert_to_date_time(i)
        temp_list.append(temp)

    stock_df['Date'] = temp_list
      #conversion Complete and Added a Coloumn in List
      
    stock_df.insert(0, 'STOCK', symbol)
    df = pd.concat([df, stock_df])

# Reset the index of the DataFrame
df.reset_index(drop=True, inplace=True)

# Display the DataFrame
print(df)
# Save DataFrame to Excel file
# output_file = 'stock_data.xlsx'
# df.to_excel(output_file, index=False)

# print("Data saved to", output_file) 



