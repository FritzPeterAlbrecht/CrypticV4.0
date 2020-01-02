from configuration import Configuration
from colorcontroller import ColorController
from metrics import Metrics
from uxcontroller import UXController
from time import sleep as s

if __name__ == "__main__":

    # setup
    config = Configuration("./config.json")
    color_config = ColorController("./colors.json")
    metrics = Metrics(config)
    uxcontroller = UXController(metrics, config, color_config)

    # Run programm

    metrics.update()
    metrics.set_dayscale()
    print("24h change:", metrics.daychange)
    print("24h Skala:", metrics.day_scale)
    #print("7d change:", metrics.get_weekchange())
    #print("7d Skala:", metrics.wscale)

    uxcontroller.roi_scale()


    # if metrics.get_weekchange() < 0.0:
    #     print("Week in the minus")
    #     uxcontroller.decrease()
    # else:
    #     print("Week in the plus")
    #     uxcontroller.increase()
    # s(2)
    # if metrics.get_daychange() < 0.0:
    #     print("Day in the minus")
    #     uxcontroller.decrease()
    # else:
    #     print("Day in the plus")
    #     uxcontroller.increase()





'''
Schlaue Kommentare bitte hier rein:

'''