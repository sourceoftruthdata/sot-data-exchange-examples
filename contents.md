# Table of Contents for /documentation

---
### Coinbase Coins Product Overview
Instructions: This code is provided for visibility into the Source of Truth AWS data collection approach.  
We have included as much detail as possible with the exception of file locations, which the user must provide.
The core of the coinbase_coins.py job is to connect with the Coinbase API and extract available coins (see code).
There is additional data from the API Response that Source of Truth will make available as necessary.

---
### Kraken Coins Product Overview
Instructions: This code is provided for visibility into the Source of Truth AWS data collection approach.  
We have included as much detail as possible with the exception of file locations, which the user must provide.
The core of the kraken_coins.py job is to connect with the Kraken API and extract available coins (see code).
There is additional data from the API Response that Source of Truth will make available as necessary.

---
## AWS Data Exchange Documentation

https://docs.aws.amazon.com/data-exchange/latest/userguide/product-description-templates.html


--
### These examples require the installation of a virutal environment, usually accomplished by entering:

>python3 -m venv venv

>source ./venv/bin/activate

>pip install -r requirements.txt

>python ./code/coinbase_coins_public.py

### The expected output is the current Coinbase Assets printed to screen.  The user can modify and request any necessary sub-fields.