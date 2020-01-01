import json
import requests
import math

class Metrics:

    def __init__(self, config):

        self.config = config
        self.daychange = float
        self.weekchange = float
        self.scale = 0.5
        self.wscale = 0.5
        self.led_count = 8
        self.led_to_lit = 0

    def update(self):

        apikey = self.config.get_api_key()
        coinid = self.config.get_coin_id()
        currency = self.config.get_currency()
        invest = self.config.get_coin_invest()
        amount = float(self.config.get_coin_amount())

        # Auskommentiert weil sonst zu viele API Calls an CMC gehen was Credits verbraucht
        #r = requests.get(
        #    'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id=' + coinid + '&convert=' + currency,
        #headers={'X-CMC_PRO_API_KEY': apikey, 'Accept': 'application/json'})

        #output = r.json()

        self.rank = 23#str(output['data'][coinid]['cmc_rank'])
        self.symbol = "IOTA"#str(output['data'][coinid]['symbol'])
        self.price = 0.145#output['data'][coinid]['quote'][currency]['price']
        self.daychange = -1.34#output['data'][coinid]['quote'][currency]['percent_change_24h']
        self.weekchange = -3.642#output['data'][coinid]['quote'][currency]['percent_change_7d']
        self.actual_value = amount * float(self.price)

        print(str(self.rank) + ' ' + str(self.symbol) + ' ' + "%.3f" % self.price + ' ' + "%.2f" % self.daychange + '% ' + "%.2f" % self.actual_value + '€')

    # Setting the scale per LED (0.5% / 1% / 2% / 4%) and returns the value of the 24h change
    def get_daychange(self):
        daychange = self.daychange

        self.scale = 4

        if daychange <= 16:
           self.scale = 2
        if daychange <= 8:
           self.scale = 1
        if daychange <= 4:
           self.scale = 0.5

        if daychange < -16:
            self.scale = 4
        if daychange >= -16:
            self.scale = 2
        if daychange >= -8:
            self.scale = 1
        if daychange >= -4:
            self.scale = 0.5
        return daychange

    # Setting the wscale per LED (0.5% / 1% / 2% / 4%) and returns the value of the 7d change
    def get_weekchange(self):
        weekchange = self.weekchange

        self.wscale = 4

        if weekchange <= 16:
            self.wscale = 2
        if weekchange <= 8:
            self.wscale = 1
        if weekchange <= 4:
            self.wscale = 0.5

        if weekchange < -16:
            self.wscale = 4
        if weekchange >= -16:
            self.wscale = 2
        if weekchange >= -8:
            self.wscale = 1
        if weekchange >= -4:
            self.wscale = 0.5
        return weekchange

    # calculate the Blinkt! LEDs to fire for the daily change
    def get_led_to_lit(self):
        self.led_to_lit = int(self.get_daychange() / self.scale)
        return self.led_to_lit

    # # calculate the Blinkt! LEDs to fire for the weekly change
    # def get_led_to_lit_week(self):
    #     self.led_to_lit_week = int(self.get_weekchange() / self.wscale)
    #     return self.led_to_lit_week

    # calculate the actual return of investment
    def get_roi(self):
        self.roi = float(self.actual_value) - float(self.config.get_coin_invest())
        return self.roi

'''
Kommentarfunktion ist eingeschaltet:

Kann später wenn das "decrease" implementiert wird die Skala trotzdem positiv Werte haben?

'''