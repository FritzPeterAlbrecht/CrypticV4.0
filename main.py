from configuration import Configuration
from colorcontroller import ColorController
from debugger import Debugger
from metrics import Metrics
from uxcontroller import UXController
from time import sleep

if __name__ == "__main__":

    while True:

        # setup
        config = Configuration("./config.json")
        color_config = ColorController("./colors.json")
        dbg = Debugger(False)
        metrics = Metrics(config, dbg)
        uxcontroller = UXController(metrics, config, color_config, dbg)

        # Run programm
        metrics.update()
        print("24h change: " + str(metrics.daychange))
        print("7d change:" + str(metrics.weekchange))

        # fire the LED Shim animation
        uxcontroller.roi_scale()
        sleep(0.5)

        # Set start parameters for Blinkt! Module Animations
        scale = 0.5
        timeout = 0.2

        # weekchange in the plus
        if metrics.weekchange > 0.0:

            dbg.print("weekchange in the plus!")

            # choose which animation to run for the week
            if metrics.weekchange <= 4:
                dbg.print("weekchange bis 4%")
                uxcontroller.increase(metrics.weekchange, scale)
                sleep(timeout)

            elif metrics.weekchange <= 8:
                dbg.print("weekchange bis 8%")
                for i in range(0,2):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.increase(metrics.weekchange, scale)
                    sleep(timeout)
                    scale *= 2

            elif metrics.weekchange <= 16:
                dbg.print("weekchange bis 16%")
                for i in range(0,3):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.increase(metrics.weekchange, scale)
                    sleep(timeout)
                    scale *= 2

            else: # weekchange > 16
                dbg.print("weekchange bis 32%")
                for i in range(0,4):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.increase(metrics.weekchange, scale)
                    sleep(timeout)
                    scale *= 2

        # weekchange in the minus
        if metrics.weekchange < 0.0:

            # choose which animation to run for the week

            if metrics.weekchange >= -4:
                dbg.print("weekchange bis -4%")
                uxcontroller.decrease(metrics.weekchange, scale)
                sleep(timeout)

            elif metrics.weekchange >= -8:
                dbg.print("weekchange bis -8%")
                for i in range(0,2):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.decrease(metrics.weekchange, scale)
                    sleep(timeout)
                    scale *= 2

            elif metrics.weekchange >= -16:
                dbg.print("weekchange bis -16%")
                for i in range(0,3):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.decrease(metrics.weekchange, scale)
                    sleep(timeout)
                    scale *= 2

            else: # > -16:
                dbg.print("weekchange bis -32%")
                for i in range(0,4):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.decrease(metrics.weekchange, scale)
                    sleep(timeout)
                    scale *= 2

        scale = 0.5 # had to reset the scale, dig further later
        sleep(2)

        # daychange in the plus
        if metrics.daychange > 0.0:

            dbg.print("daychange in the plus!")

            # choose which animation to run for the day
            if metrics.daychange <= 4:
                dbg.print("daychange bis 4%")
                uxcontroller.increase(metrics.daychange, scale)
                sleep(timeout)

            elif metrics.daychange <= 8:
                dbg.print("daychange bis 8%")
                for i in range(0,2):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.increase(metrics.daychange, scale)
                    sleep(timeout)
                    scale *= 2

            elif metrics.daychange <= 16:
                dbg.print("daychange bis 16%")
                for i in range(0,3):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.increase(metrics.daychange, scale)
                    sleep(timeout)
                    scale *= 2

            else: # daychange > 16
                dbg.print("daychange bis 32%")
                for i in range(0,4):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.increase(metrics.daychange, scale)
                    sleep(timeout)
                    scale *= 2

        # daychange in the minus
        elif metrics.daychange < 0.0:
            dbg.print("day in the minus")

            # choose which animation to run for the day
            if metrics.daychange >= -4:
                dbg.print("daychange bis -4%")
                uxcontroller.decrease(metrics.daychange, scale)
                sleep(timeout)

            elif metrics.daychange >= -8:
                dbg.print("daychange bis -8%")
                for i in range(0,2):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.decrease(metrics.daychange, scale)
                    sleep(timeout)
                    scale *= 2

            elif metrics.daychange >= -16:
                dbg.print("daychange bis -16%")
                for i in range(0,3):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.decrease(metrics.daychange, scale)
                    sleep(timeout)
                    scale *= 2

            else: # > -16:
                dbg.print("daychange bis -32%")
                for i in range(0,4):
                    dbg.print("Skala:" + str(scale))
                    uxcontroller.decrease(metrics.daychange, scale)
                    sleep(timeout)
                    scale *= 2
        
        uxcontroller.scroller()
        sleep(400)
