import time

class UXController:

    def __init__(self, metrics, config, color_controller, dbg):

        self.dbg = dbg

        self.metrics = metrics
        self.config = config
        self.color_controller = color_controller
        self.blinkt_speed = 0.1

    # function for Blinkt! Module animation if change has positive value
    def increase(self, change, scale):

        rate = round(change / scale)
        led_limit = rate if rate < 8 else 8

        print("--------->" + str(led_limit))

        self.dbg.print("Number of value: " + str(scale) + " " + "LEDs: " + str(led_limit))

        if scale == 4:
            self.dbg.print("Color Set Four Red:" + str(self.color_controller.get_four_up_red()))

            self.dbg.print("Color Set Four Green:" + str(self.color_controller.get_four_up_green()))

            self.dbg.print("Color Set Four Blue:" + str(self.color_controller.get_four_up_blue()))

        if scale == 2:
            self.dbg.print("Color Set Two Red:" + str(self.color_controller.get_two_up_red()))

            self.dbg.print("Color Set Two Green:" + str(self.color_controller.get_two_up_green()))

            self.dbg.print("Color Set Two Blue:" + str(self.color_controller.get_two_up_blue()))

        if scale == 1:
            self.dbg.print("Color Set One Red:" + str(self.color_controller.get_one_up_red()))

            self.dbg.print("Color Set One Green:" + str(self.color_controller.get_one_up_green()))

            self.dbg.print("Color Set One Blue:" + str(self.color_controller.get_one_up_blue()))

        if scale == 0.5:
            self.dbg.print("Color Set Half Red:" + str(self.color_controller.get_half_up_red()))

            self.dbg.print("Color Set Half Green:" + str(self.color_controller.get_half_up_green()))

            self.dbg.print("Color Set Half Blue:" + str(self.color_controller.get_half_up_blue()))

        duration = self.blinkt_speed

        for i in range(0, led_limit):

            self.dbg.print(i)
            time.sleep(duration)

            # slow down iteration time set in config
            duration += self.config.blinkt_speed_decrease

    # function for Blinkt! Module animation if change has negative value
    def decrease(self, change, scale):

        rate = round(change / scale)
        led_limit = rate if rate > -8 else -8

        self.dbg.print("Number of value" + " " + str(scale) + " LEDs: " + str(rate))

        duration = self.blinkt_speed
        i = 0

        while i > rate:
            self.dbg.print(i)
            time.sleep(duration)

            # slow down iteration time set in config
            duration += self.config.blinkt_speed_decrease
            i -= 1

            if i == -8:
                break



    # Animate the return of invest on the LED Shim
    def roi_scale(self):
        pixel_value = int(int(self.config.get_coin_invest()) / 28)
        pixel_count = int(self.metrics.actual_value / pixel_value)
        self.dbg.print("Value per ROI LED: " + str(pixel_value) + "\nNumber of ROI LED:" + str(pixel_count))

'''
Kommentare:
zwischenzeitlicg hast du nicht auch main geändert? die weekchages und daychanges? Es lief alles. Nachdem ich in main alles erweitert hatte und decrease angepasst, vielleicht ists aber auch einfach ein bug bei verschiedenen werten... ich teste das jetzt mal
'''
