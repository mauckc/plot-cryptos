from subprocess import call
import time
import os
# Sample call
# wget -O data/bittrex/hour/Bittrex_XRPETH_1h.csv https://www.cryptodatadownload.com/cdd/Bittrex_XRPETH_1h.csv
# Configure OS paths
import csv

# Set hour market pairs
bittrex_USDpair_markets = ['BTCUSD','ETHUSD','LTCUSD','NEOUSD','ETCUSD','OMGUSD','XMRUSD','DASHUSD']
bittrex_BTCpair_markets = ['XRPBTC','ETHBTC','LTCBTC','NEOBTC','NXTBTC','ETCBTC','ZECBTC','XLMBTC','WAVESBTC','ADABTC']
bittrex_ETHpair_markets = ['XRPETH','LTCETH','NEOETH','ZECETH','XLMETH','ADAETH','DASHETH','PAYETH','SALTETH','XMRETH','OMGETH']

required_data_path = './data/bittrex/hour/'
if not os.path.exists(required_data_path):
    os.makedirs(required_data_path)
requiredfiles = [f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f)) if 'Bittrex' in f ]
# Check if files exist initially, if they do not then create placeholders
if len(requiredfiles) == 0:
    print('[ERR]: No files exist.')
    markets = bittrex_USDpair_markets + bittrex_BTCpair_markets + bittrex_ETHpair_markets
    for market in markets:
        with open(required_data_path + 'Bittrex_'+ market +'_1h.csv', 'wb') as csvfile:
            samplewriter = csv.writer(csvfile, delimiter=' ',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            samplewriter.writerow(['Spam'] * 5 + ['Baked Beans'])
            samplewriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

    requiredfiles = [f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f)) if 'Bittrex' in f ]

# Update relative paths
requiredfilespaths =  [ required_data_path + f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f))]

# Configure the download paths
download_path = "https://www.cryptodatadownload.com/cdd/"
download_files_path =  [ download_path + f for f in requiredfiles]

# Run forever! by opening the stream
while True:
    for i, file in enumerate(requiredfiles):
        output_path = requiredfilespaths[i]
        get_download_path = download_files_path[i]
        print(output_path)
        print(get_download_path)
        # Make shell call to download the file
        call(["wget","--no-check-certificate", "-O", output_path, get_download_path])
        time.sleep(2)

    # Sleep for an hour
    time.sleep(60*60)
