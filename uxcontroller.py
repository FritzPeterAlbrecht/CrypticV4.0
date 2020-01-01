import time

class UXController:

    def __init__(self, metrics, config, color_controller):

        self.config = config
        self.metrics = metrics
        self.blinkt_speed = 0.1
        self.color_controller = color_controller


    # function for Blinkt! Module animation if change has positive value
    def increase(self):
        self.led_to_lit = self.metrics.get_led_to_lit()

        print("Number of value", self.metrics.scale, "LEDs:", self.metrics.led_to_lit)
        if self.metrics.scale == 4:
            print("Color Set Four Red:", self.color_controller.get_four_up_red())
            print("Color Set Four Green:", self.color_controller.get_four_up_green())
            print("Color Set Four Blue:", self.color_controller.get_four_up_blue())
        if self.metrics.scale == 2:
            print("Color Set Two Red:", self.color_controller.get_two_up_red())
            print("Color Set Two Green:", self.color_controller.get_two_up_green())
            print("Color Set Two Blue:", self.color_controller.get_two_up_blue())
        if self.metrics.scale == 1:
            print("Color Set One Red:", self.color_controller.get_one_up_red())
            print("Color Set One Green:", self.color_controller.get_one_up_green())
            print("Color Set One Blue:", self.color_controller.get_one_up_blue())
        if self.metrics.scale == 0.5:
            print("Color Set Half Red:", self.color_controller.get_half_up_red())
            print("Color Set Half Green:", self.color_controller.get_half_up_green())
            print("Color Set Half Blue:", self.color_controller.get_half_up_blue())

        duration = self.blinkt_speed

        for i in range(0, self.led_to_lit):
            print(i)
            time.sleep(duration)
            duration += self.config.blinkt_speed_decrease # slow down iteration time set in config

    # function for Blinkt! Module animation if change has negative value
    def decrease(self):
        self.led_to_lit = self.metrics.get_led_to_lit()
        print("Number of value", self.metrics.wscale, "LEDs:", self.metrics.led_to_lit)

        duration = self.blinkt_speed
        i = 0

        while i > self.led_to_lit:
            print(i)
            time.sleep(duration)
            duration += self.config.blinkt_speed_decrease # slow down iteration time set in config
            i = i - 1
            if i == self.led_to_lit:
                break

    # Animate the return of invest on the LED Shim
    def roi_scale(self):
        pixel_value = int(int(self.config.get_coin_invest()) / 28)
        pixel_count = int(self.metrics.actual_value / pixel_value)
        print("Value per ROI LED:", pixel_value, "\nNumber of ROI LED:", pixel_count)

    # def scroller(self):
    #     pass
