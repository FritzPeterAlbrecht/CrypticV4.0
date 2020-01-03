import json

# Class to load and return the color values for the Blinkt! and LED Shim Module
class ColorController:

    def __init__(self, filename = "./colortables.json"):

        self.load_colors(filename)

    def load_colors(self, filename):

        with open(filename, 'r') as f:
            ct = json.load(f)

            # colors for positive Blinkt! values
            self.half_up_red = ct["half_up"]["r"]
            self.half_up_green = ct["half_up"]["g"]
            self.half_up_blue = ct["half_up"]["b"]

            self.one_up_red = ct["one_up"]["r"]
            self.one_up_green = ct["one_up"]["g"]
            self.one_up_blue = ct["one_up"]["b"]

            self.two_up_red = ct["two_up"]["r"]
            self.two_up_green = ct["two_up"]["g"]
            self.two_up_blue = ct["two_up"]["b"]

            self.four_up_red = ct["four_up"]["r"]
            self.four_up_green = ct["four_up"]["g"]
            self.four_up_blue = ct["four_up"]["b"]

            # Colors for negative Blinkt! values
            self.half_down_red = ct["half_down"]["r"]
            self.half_down_green = ct["half_down"]["g"]
            self.half_down_blue = ct["half_down"]["b"]

            self.one_down_red = ct["one_down"]["r"]
            self.one_down_green = ct["one_down"]["g"]
            self.one_down_blue = ct["one_down"]["b"]

            self.two_down_red = ct["two_down"]["r"]
            self.two_down_green = ct["two_down"]["g"]
            self.two_down_blue = ct["two_down"]["b"]

            self.four_down_red = ct["four_down"]["r"]
            self.four_down_green = ct["four_down"]["g"]
            self.four_down_blue = ct["four_down"]["b"]

            # colors for the LED Shim
            self.shim_red = ct["led_shim"]["r"]
            self.shim_green = ct["led_shim"]["g"]
            self.shim_blue = ct["led_shim"]["b"]

    # return colors for positive Blinkt! values
    def get_half_up_red(self):
        return self.half_up_red
    def get_half_up_green(self):
        return self.half_up_green
    def get_half_up_blue(self):
        return self.half_up_blue

    def get_one_up_red(self):
        return self.one_up_red
    def get_one_up_green(self):
        return self.one_up_green
    def get_one_up_blue(self):
        return self.one_up_blue

    def get_two_up_red(self):
        return self.two_up_red
    def get_two_up_green(self):
        return self.two_up_green
    def get_two_up_blue(self):
        return self.two_up_blue

    def get_four_up_red(self):
        return self.four_up_red
    def get_four_up_green(self):
        return self.four_up_green
    def get_four_up_blue(self):
        return self.four_up_blue

    # return colors for negative Blinkt! values
    def get_half_down_red(self):
        return self.half_down_red
    def get_half_down_green(self):
        return self.half_down_green
    def get_half_down_blue(self):
        return self.half_down_blue

    def get_one_down_red(self):
        return self.one_down_red
    def get_one_down_green(self):
        return self.one_down_green
    def get_one_down_blue(self):
        return self.one_down_blue

    def get_two_down_red(self):
        return self.two_down_red
    def get_two_down_green(self):
        return self.two_down_green
    def get_two_down_blue(self):
        return self.two_down_blue

    def get_four_down_red(self):
        return self.four_down_red
    def get_four_down_green(self):
        return self.four_down_green
    def get_four_down_blue(self):
        return self.four_down_blue

    # return the color values for LED Shim Module
    def get_led_shim_red(self):
        return self.shim_red
    def get_led_shim_green(self):
        return self.shim_green
    def get_led_shim_blue(self):
        return self.shim_blue
