# plot-cryptos
Plotting metrics for crypto data


## Sample Output

![Crypto Plot Sample](./output/Bittrex_BTCUSD_1h_2018-04-30_23-00-00_to_2018-03-31_00-00-00.png)

## The Code
```Python
# Check for data files and Sort out paths
required_data_path = './data/bittrex/hour/'
requiredfiles = [f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f)) if 'Bittrex' in f ]
requiredfilespaths =  [ required_data_path + f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f))]

# Read the files from excel spreadsheets
l_dfs = [fix_bittrex_dates(pd.DataFrame(read_bittrex(data_path))) for data_path in requiredfilespaths]
# Do some processing on the dates but not currently for future use
required_start_date = l_dfs[0].Date.min()
required_end_date = l_dfs[0].Date.max()
required_dates = pd.date_range(required_start_date, required_end_date, freq='M')
# Output that information
print('\nRequired Data Start Date: {}'.format(required_start_date))
print('Required Data End Date: {}\n'.format(required_end_date))
```

```Python
# Iterate through all of the data files found use index to match name of input file
for i, df in enumerate(l_dfs,0):
    # Process Raw Data
    df = fix_bittrex_dates(df)

    # Assign parameters
    price = df['Close']    # Choose which price data to plot
    metric_time_delta = 30    # Choose the time averaged for Mean Average and Mean Standard Deviation
    start_date_1 = '1/1/2018'    # Choose first start date time
    start_date_2 = '2/1/2018'    # Choose second start date time
    num_periods = 3    # Choose number of intervals to plot
    time_freq = 'M'    # Choose time-series range of each individual plot
    date_format ='%Y-%m-%d'    # Choose how the dates are formatted
    
    # Process the assigned parameters 
    dates = zip_dates(start_date_1, start_date_2, num_periods, time_freq, date_format)
    # Calculate the mean and standard deviation
    ma = price.rolling(metric_time_delta).mean()
    mstd = price.rolling(metric_time_delta).std()

    # plot each set of dates
    for day1, day2 in dates:
        thisdf = df.loc[day1:day2, :]
        crypto_plot(thisdf, requiredfiles[i])

```

![Crypto Plot Sample](./output/Bittrex_XRPETH_1h_2018-03-31_23-00-00_to_2018-02-28_00-00-00.png)
