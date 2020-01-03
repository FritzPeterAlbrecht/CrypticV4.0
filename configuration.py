import json

class Configuration:

    def __init__(self, filename = "./config.json"):
        self.load(filename)

    def load(self, filename):

        with open(filename, 'r') as f:
            c = json.load(f)

            print("loaded configuration: ", c)

            # API Key for your Coin Market Cap Account
            self.api_key = c["APIKey"]
            # ID of your Coin
            self.coin_id = c["CoinID"]
            # Currency for conversion
            self.currency = c["Currency"]
            # Investment in Fiat
            self.invest = c["CoinInvest"]
            # Amount of tokens
            self.coin_amount = c["CoinAmount"]
            # Speed of the Textscroller on Scrollphat HD
            self.scroller_speed = c["ScrollerSpeed"]
            # Brightness of the Scrollphat HD
            self.scroller_brightness = c["ScrollerBrightness"]
            # Main Speed of the Blinkt! Animatons
            self.blinkt_speed = c["BlinktSpeed"]
            # Slowdown of the Blinkt! animation with increasing value
            self.blinkt_speed_decrease = c["BlinktSpeedDecrease"]
            # Brightness of the Blinkt! Module
            self.blinkt_brightness = c["BlinktBrightness"]
            # LED Shim Animation Speed
            self.shim_speed = c["LEDShimSpeed"]
            # LED Shim Animation Speed Decrease
            self.shim_speed_decrease = c["LEDShimSpeedDecrease"]


    def get_api_key(self):
        return self.api_key

    def get_coin_id(self):
        return self.coin_id

    def get_currency(self):
        return self.currency

    def get_coin_invest(self):
        return self.invest

    def get_coin_amount(self):
        return self.coin_amount

    def get_scroller_speed(self):
        return self.scroller_speed

    def get_scroller_brightness(self):
        return self.scroller_brightness

    def get_blinkt_speed(self):
        return self.blinkt_speed

    def get_blinkt_speed_decrease(self):
        return self.blinkt_speed_decrease

    def get_blinkt_brightness(self):
        return self.blinkt_brightness

    def get_led_shim_speed(self):
        return self.shim_speed

    def get_led_shim_speed_decrease(self):
        return self.shim_speed_decrease
