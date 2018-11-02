from subprocess import call
import time
import os
# Sample call
# wget -O data/bittrex/hour/Bittrex_XRPETH_1h.csv https://www.cryptodatadownload.com/cdd/Bittrex_XRPETH_1h.csv
# Configure OS paths
required_data_path = './data/bittrex/hour/'
requiredfiles = [f for f in os.listdir(required_data_path) if os.path.isfile(os.path.join(required_data_path, f)) if 'Bittrex' in f ]
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
        time.sleep(3)
    # Sleep for an hour
    time.sleep(60*60)
