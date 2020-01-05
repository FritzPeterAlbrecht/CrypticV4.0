import time
import blinkt
import scrollphat
import ledshim


################################################################################
###### The UX Controller controls all the hardware parts in Cryptic V4.0 #######
################################################################################

class UXController:

    def __init__(self, metrics, config, color_controller, dbg):

        self.dbg = dbg

        self.metrics = metrics
        self.config = config
        self.color_controller = color_controller

################################################################################

    # function for Blinkt! Module animation if change has positive value
    def increase(self, change, scale):

        bright = self.config.blinkt_brightness

        blinkt.clear()
        blinkt.show()

        rate = round(change / scale)
        led_limit = rate if rate < 8 else 8

        # set the colors for scale 4
        if scale == 4:

            r = self.color_controller.get_four_up_red()
            self.dbg.print("Color Set Four Red:" + str(r))

            g = self.color_controller.get_four_up_green()
            self.dbg.print("Color Set Four Green:" + str(g))

            b = self.color_controller.get_four_up_blue()
            self.dbg.print("Color Set Four Blue:" + str(b))

        #set the colors for scale 2
        if scale == 2:

            r = self.color_controller.get_two_up_red()
            self.dbg.print("Color Set Two Red:" + str(r))

            g = self.color_controller.get_two_up_green()
            self.dbg.print("Color Set Two Green:" + str(g))

            b = self.color_controller.get_two_up_blue()
            self.dbg.print("Color Set Two Blue:" + str(b))

        # set the colors for scale 1
        if scale == 1:

            r = self.color_controller.get_one_up_red()
            self.dbg.print("Color Set One Red:" + str(r))

            g = self.color_controller.get_one_up_green()
            self.dbg.print("Color Set One Green:" + str(g))

            b = self.color_controller.get_one_up_blue()
            self.dbg.print("Color Set One Blue:" + str(b))

        # set the colors for scale .5
        if scale == 0.5:

            r = self.color_controller.get_half_up_red()
            self.dbg.print("Color Set Half Red:" + str(r))

            g = self.color_controller.get_half_up_green()
            self.dbg.print("Color Set Half Green:" + str(g))

            b = self.color_controller.get_half_up_blue()
            self.dbg.print("Color Set Half Blue:" + str(b))

        duration = self.config.blinkt_speed

        ln = 7

        for i in range(0, led_limit):

            blinkt.set_pixel(ln, r[ln], g[ln], b[ln], brightness = bright)
            blinkt.show()
            self.dbg.print(ln)
            ln -= 1
            time.sleep(duration)

            # slow down iteration time set in config
            duration += self.config.blinkt_speed_decrease

################################################################################

    # function for Blinkt! Module animation if change has negative value
    def decrease(self, change, scale):

        bright = self.config.blinkt_brightness

        blinkt.clear()
        blinkt.show()

        rate = round(change / scale)
        led_limit = rate if rate > -8 else -8

        self.dbg.print("Number of value" + " " + str(scale) + " LEDs: " + str(rate))

        # set the negative colors for scale 4
        if scale == 4:

            r = self.color_controller.get_four_down_red()
            self.dbg.print("Color Set Four Red:" + str(r))

            g = self.color_controller.get_four_down_green()
            self.dbg.print("Color Set Four Green:" + str(g))

            b = self.color_controller.get_four_down_blue()
            self.dbg.print("Color Set Four Blue:" + str(b))

        #set the negative colors for scale 2
        if scale == 2:

            r = self.color_controller.get_two_down_red()
            self.dbg.print("Color Set Two Red:" + str(r))

            g = self.color_controller.get_two_down_green()
            self.dbg.print("Color Set Two Green:" + str(g))

            b = self.color_controller.get_two_down_blue()
            self.dbg.print("Color Set Two Blue:" + str(b))

        # set the negative colors for scale 1
        if scale == 1:

            r = self.color_controller.get_one_down_red()
            self.dbg.print("Color Set One Red:" + str(r))

            g = self.color_controller.get_one_down_green()
            self.dbg.print("Color Set One Green:" + str(g))

            b = self.color_controller.get_one_down_blue()
            self.dbg.print("Color Set One Blue:" + str(b))

        # set the negative colors for scale .5
        if scale == 0.5:

            r = self.color_controller.get_half_down_red()
            self.dbg.print("Color Set Half Red:" + str(r))

            g = self.color_controller.get_half_down_green()
            self.dbg.print("Color Set Half Green:" + str(g))

            b = self.color_controller.get_half_down_blue()
            self.dbg.print("Color Set Half Blue:" + str(b))

        duration = self.config.blinkt_speed

        i = 0
        ln = 0

        while i > rate:

            blinkt.set_pixel(ln, r[ln], g[ln], b[ln], brightness = bright)
            blinkt.show()

            self.dbg.print(ln)

            i -= 1
            ln += 1
            time.sleep(duration)

            # slow down iteration time set in config
            duration += self.config.blinkt_speed_decrease

            if i == -8:
                i = 0
                ln = 0
                break

################################################################################

    # Animate the return of invest on the LED Shim
    def roi_scale(self):

        pixel_value = int(int(self.config.get_coin_invest()) / 28)
        pixel_count = int(self.metrics.actual_value / pixel_value)

        bright = self.config.shim_bright

        ledshim.clear()
        ledshim.show()

        self.dbg.print("Value per ROI LED: " + str(pixel_value) + "\nNumber of ROI LED:" + str(pixel_count))

        r = self.color_controller.get_led_shim_red()
        self.dbg.print("r: " + str(r))
        g = self.color_controller.get_led_shim_green()
        self.dbg.print("g: " + str(g))
        b = self.color_controller.get_led_shim_blue()
        self.dbg.print("b: " + str(b))

        duration = self.config.shim_speed

        ln = 27

        for i in range(pixel_count):
            self.dbg.print(ln)
            ledshim.set_pixel(ln, r[ln], g[ln], b[ln], brightness = bright)
            ledshim.show()

            time.sleep(duration)

            ln -= 1

            if ln == 0:
                ln = 27
                break

            # slow down iteration time set in config
            duration += self.config.shim_speed_decrease

################################################################################

    def scroller(self):

        if self.metrics.price >= 0.36:

            scrollphat.clear()
            scrollphat.show()
            scrollphat.write_string('HODL', x=0, y=0, brightness=1.0)
            scrollphat.show()

        else:

            loopcounter = 0
            loop = 500
            text = self.metrics.ticker

            print(text)

            scrollphat.clear()
            scrollphat.show()

            scrollphat.write_string(text, x=50, y=0, brightness = 0.18)

            scrollphat.rotate(180)

            while loopcounter != loop:

                scrollphat.show()
                scrollphat.scroll(1)
                time.sleep(0.024)
                loopcounter = loopcounter + 1

                if loopcounter == loop:
                    scrollphat.clear()
                    scrollphat.show()
                    break
