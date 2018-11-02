
import pandas as pd
import numpy as np
#from pandas_datareader import data as web
import matplotlib.pyplot as plt
from datetime import datetime, date, time
import os
import string

def fix_bittrex_dates(df_crypto):
    #set an index by dates
    df_crypto['Date'] = pd.to_datetime(df_crypto['Date'], format="%Y-%m-%d %I-%p", errors='coerce')
    df_crypto.index = df_crypto['Date']
    return df_crypto

def read_bittrex(crypto_path):
    df_crypto = pd.read_csv(crypto_path, low_memory=False, header=1)
    print(df_crypto.tail()) # Show data loading in
    return fix_bittrex_dates(df_crypto)

def zip_dates(start_date_1, start_date_2, num_periods, time_freq, date_format):
    dates = zip(pd.date_range(start=start_date_1, periods=num_periods, freq=time_freq).format(formatter=lambda x: x.strftime(date_format)),pd.date_range(start=start_date_2, periods=num_periods, freq=time_freq).format(formatter=lambda x: x.strftime(date_format)))
    return dates

def crypto_plot(thisdf, crypto_market, metric_time_delta):
    # thisdf.index = thisdf['Date']
    price = thisdf['Close']
    ma = price.rolling(metric_time_delta).mean()
    mstd = price.rolling(metric_time_delta).std()

    plt.figure(2,figsize=(12,6))
    fill_plt = plt.fill_between(mstd.index, ma-2*mstd, ma+2*mstd, color='b', alpha=0.2)
    plt.plot(price.index, price, 'k', ma.index, ma, 'b')
    plt.grid()
    # plt.xlabel('Hours')
    plt.ylabel(''.join((crypto_market.replace('.csv','')[8:14],)))
    plt.title(''.join((crypto_market.replace('.csv',''),' ',str(pd.to_datetime(thisdf.Date.values[0])).replace(':','-'), ' to ',str(pd.to_datetime(thisdf.Date.values[-1])))).replace('_',' '))
    plt.savefig(''.join(('output/',crypto_market.replace('.csv',''),' ',str(pd.to_datetime(thisdf.Date.values[0])).replace(':','-'), ' to ',str(pd.to_datetime(thisdf.Date.values[-1])),'.png')).replace(':','-').replace(' ','_'))
    plt.show()

## Check for data files
required_data_path = './data/bittrex/hour/'
requiredfiles = [f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f)) if 'Bittrex' in f ]
requiredfilespaths =  [ required_data_path + f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f))]
# Read the files from excel spreadsheets
l_dfs = [fix_bittrex_dates(pd.DataFrame(read_bittrex(data_path))) for data_path in requiredfilespaths]

required_start_date = l_dfs[0].Date.min()
required_end_date = l_dfs[0].Date.max()
required_dates = pd.date_range(required_start_date, required_end_date, freq='M')

print('\nRequired Data Start Date: {}'.format(required_start_date))
print('Required Data End Date: {}\n'.format(required_end_date))

for i, df in enumerate(l_dfs,0):
    metric_time_delta = 30
    start_date_1 = '1/1/2018'
    start_date_2 = '2/1/2018'
    num_periods = 3
    time_freq = 'M'
    date_format ='%Y-%m-%d'

    dates = zip_dates(start_date_1, start_date_2, num_periods, time_freq, date_format)

    for day1, day2 in dates:
        thisdf = df.loc[day1:day2, :]
        crypto_plot(thisdf, requiredfiles[i], metric_time_delta)
