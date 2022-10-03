#################
# Import packages
#################

import requests
import pandas as pd
from datetime import datetime

# set runtime info
today = datetime.now()
runtime = today.strftime("%m-%d-%Y %H:%M")

# Define main
def main():

    uri = 'https://api.kraken.com/0/public/AssetPairs'
    response = requests.get(uri).json()

    coins=(pd.DataFrame.from_dict(response['result']).T)
    coins=pd.DataFrame((coins[coins['quote']=='ZUSD']).reset_index()['base'])
    coins['runtime']=runtime
    coins.columns=['coin', 'runtime']
    coins=coins.sort_values(by='coin').reset_index(drop=True)

    #########################
    # print current coins from API
    #########################

    print(coins)

# Main
if __name__ == '__main__':
    main()