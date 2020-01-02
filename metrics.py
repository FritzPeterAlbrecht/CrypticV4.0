import json
import requests
import math

class Metrics:

    def __init__(self, config):

        self.config = config
        self.daychange = float
        self.weekchange = float
        self.day_scale = 0
        self.week_scale = 0
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
        self.daychange = 25.34#output['data'][coinid]['quote'][currency]['percent_change_24h']
        self.weekchange = 3.642#output['data'][coinid]['quote'][currency]['percent_change_7d']
        self.actual_value = amount * float(self.price)
        self.ticker = str(self.rank) + ' ' + str(self.symbol) + ' ' + "%.3f" % self.price + ' ' + "%.2f" % self.daychange + '% ' + "%.2f" % self.actual_value + '€'

    # Setting the day_scale per LED (0.5% / 1% / 2% / 4%)
    def set_dayscale(self):
        daychange = self.daychange

        if daychange > 0.0:
            print("Day in the plus")
            self.day_scale = 4

            if daychange <= 16:
                self.day_scale = 2
            if daychange <= 8:
                self.day_scale = 1
            if daychange <= 4:
                self.day_scale = 0.5


        if daychange < 0.0:
            print("Day in the minus")

            if daychange < -16:
                self.day_scale = 4
            if daychange >= -16:
                self.day_scale = 2
            if daychange >= -8:
                self.day_scale = 1
            if daychange >= -4:
                self.day_scale = 0.5


    # Setting the week_scale per LED (0.5% / 1% / 2% / 4%)
        weekchange = self.weekchange

        self.week_scale = 4

        if weekchange <= 16:
            self.week_scale = 2
        if weekchange <= 8:
            self.week_scale = 1
        if weekchange <= 4:
            self.week_scale = 0.5

        if weekchange < -16:
            self.week_scale = 4
        if weekchange >= -16:
            self.week_scale = 2
        if weekchange >= -8:
            self.week_scale = 1
        if weekchange >= -4:
            self.week_scale = 0.5
        return self.week_scale

    # # calculate the Blinkt! LEDs to fire for the daily change
    # def get_led_to_lit(self):
    #     self.led_to_lit = int(self.get_daychange() / self.scale)
    #     return self.led_to_lit

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

'''