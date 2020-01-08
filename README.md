## CrypticV4.0

Crypto Coin Ticker for a Raspberry Pi or Zero WH  with a Scrollphat HD, LEDShim, and one Blinkt! Module

#### Prerequisites

1 Blinkt Module - https://shop.pimoroni.de/products/blinkt

1 LEDShim - https://shop.pimoroni.de/products/led-shim

1 ScrollphatHD - https://shop.pimoroni.de/products/scroll-phat-hd

1 Pico Hat Hacker - https://shop.pimoroni.de/products/pico-hat-hacker

1 Pin Extension - https://shop.pimoroni.de/products/male-40-pin-2x20-hat-header?variant=19570193348

#### Features

The Blinkt! 8 LED module you will show the daily and weekly change of your chosen coin in four different scales: 0.5% / 1% / 2% / 4% per LED - so you have a minimum percentual change of 0.5% and maximum percentual change of 32%. Depending on the direction of the animation and the color range you can read if it shows a positive or negative value.

The LEDShim will show the ROI - Return on Investment on a 28 LED scale. 

The ScrollphatHD will be used as for a scrolling ticker like this: [rank] - ticker symbol - actual Price - daily change % - total value of your coins

You can set the colors in the colors.json and some more settings in the config.json




#### Configuration file in json for settings

| Setting | Function |
| ------- | -------- |
| APIKey | In order to make Cryptic V4.0 work, you need an account at "https://coinmarketcap.com/api/" |
| CoinID | coin ID from CMC you want to track | 
| Currency | currency conversion for example "USD", "GBP" or "BTC". There are many conversions possible |
| CoinInvest | To calculate the "return of investment" you need to set the amount of paid fiat |
| CoinAmount | The amount of your holdings (Tokens) |
| ScrollerSpeed | sets the speed of the scrolling ticker an the scrollphat HD |
| ScrollerBrightness | brightness of the scrollphat HD |
| BlinktBrightness | brightness of the blinkt module |
| BlinktSpeed | basic speed of the blinkt animations (7 day / 24 h) |
| BlinktSpeedDecrease | slow down the speed of the blinkt with every LED which lites up |
| BlinktSeqBreak | sets the break between the different blinkt percentage scales in seconds |
| BlinktWeekDayBreak | sets the break time between 7 Day and 24h animations on the blinkt in seconds |
| LEDShimBrightness | sets the brightness of the LED Shim |
| LEDShimSpeed | basic speed of the LED Shim animation |
| LEDShimSpeedDecrease | sets the slowdown of the LED Shim animation |

#### Example configuration for the Blinkt! colors

Depending on the up or down animation, the direction of the colors maybe right to left or vice versa:

...for the positive value animations...

```
"half_up":
    {
        "r": [0, 0, 0, 0, 0, 0, 0, 0],
        "g": [160, 140, 120, 80, 40, 20, 10, 0],
        "b": [200, 200, 200, 220, 220, 250, 250, 250]
    },
          End----------------------------------------Start
```
...for the negative value animations...
```
"half_down":
    {
        "r": [10, 20, 40, 80, 120, 160, 200, 230],
        "g": [0, 0, 0, 0, 0, 0, 0, 0],
        "b": [250, 230, 210, 200, 180, 160, 150, 130]
    },
          Start----------------------------------------End
```
...and for the LED Shim.
```
"led_shim":
    {
        "r": [0, 0, 0, 0, 210, 200, 190, 180, 170, 160, 150, 140, 130, 120, 140, 140, 140, 150, 160, 160, 140, 120, 100, 80, 60, 40, 20, 0],
        "g": [250, 230, 220, 210, 190, 180, 160, 140, 120, 100, 80, 60, 40, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        "b": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 210, 240, 250]
    }
            End----------------------------------------------------------------------------------------------------------Start
```

So if you want to change your colors, make sure you are following the directions for the different animations otherwise it can be confusing.

#### Dependencies

In order to run Cryptic V4.0 you need to install some modules on your system.

Install the Python3 Blinkt Library
```sh
$ sudo pip3 install blinkt
```

Install the Python3 LED Shim Library
```sh
$ sudo pip3 install buttonshim
```

Install the Pythno3 LED Shim Library
```sh
$ sudo pip3 install scrollphathd
```

Install requests
```sh
$ pip3 install requests
```
