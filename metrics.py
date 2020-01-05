import json
import requests
import math


################################################################################
#### The Metrics Class is responsible for fetching and processing the Data #####
################################################################################

class Metrics:

    def __init__(self, config, dbg):

        self.dbg = dbg

        self.config = config
        self.daychange = float
        self.weekchange = float
        self.led_count = 8
        self.led_to_lit = 0

    # API Call Coinmarketcap.com and get all data for the set coin
    def update(self):

        apikey = self.config.get_api_key()
        coinid = self.config.get_coin_id()
        currency = self.config.get_currency()
        invest = self.config.get_coin_invest()
        amount = float(self.config.get_coin_amount())

        # API Call to coinmarketcap.com
        r = requests.get(
            'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + coinid + '&convert=' + currency,
        headers={'X-CMC_PRO_API_KEY': apikey, 'Accept': 'application/json'})

        output = r.json()

        self.rank = str(output['data'][coinid]['cmc_rank'])
        self.symbol = str(output['data'][coinid]['symbol'])
        self.price = output['data'][coinid]['quote'][currency]['price']
        self.daychange = output['data'][coinid]['quote'][currency]['percent_change_24h']

        self.weekchange = output['data'][coinid]['quote'][currency]['percent_change_7d']

        self.actual_value = amount * float(self.price)

        # construct the string for Scrollphat HD Ticker
        self.ticker = str(self.rank) + ' ' + str(self.symbol) + ' ' + "%.3f" % self.price + ' ' + "%.2f" % self.daychange + '% ' + "%.2f" % self.actual_value + '€'

# calculate the actual return of investment
    def get_roi(self):
        self.roi = float(self.actual_value) - float(self.config.get_coin_invest())
        return self.roi
