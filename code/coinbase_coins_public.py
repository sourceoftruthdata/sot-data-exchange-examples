#################
# Import packages
#################

import requests
import pandas as pd
import os
from datetime import datetime

# set runtime info
today = datetime.now()
runtime = today.strftime("%m-%d-%Y %H:%M")

# Define main
def main():

  # Instantiate DF
  coins = []

  uri = 'https://api.pro.coinbase.com/currencies'
  response = requests.get(uri).json()

  for i in range(len(response)):
      if response[i]['details']['type'] == 'crypto':
        coins.append(response[i]['id'])

  coins = pd.DataFrame(coins)
  coins['runtime']=runtime
  coins.columns=['coin', 'runtime']
  coins=coins.sort_values(by='coin').reset_index(drop=True)

  #########################
  # print current coins from API
  #########################

  print(coins)

# main
if __name__ == '__main__':
    main()