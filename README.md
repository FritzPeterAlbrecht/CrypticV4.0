## CrypticV4.0
Crypto Coin Ticker for a Raspberry Pi with a Scrollphat HD, LEDShim, and one Blinkt! Module

#### Prerequisites
1 x Blinkt Module
1 X LEDShim
1 x ScrollphatHD
1 x Pin Extension
1 x Pi Hat Hacker

#### Features
The Blinkt! 8 LED module you will see the daily and weekly change of your chosen coin in three different scales: 0.5% / 2% / 4% per LED - so you have a minimum percentual change of 0.5% and maximum percentuale change of 32%.

The LEDShim will show the ROI - Return on Investment on a 28 LED scale.

The ScrollphatHD will be used as for a scrolling ticker like this: [rank] - ticker symbol - actual Price - daily change % - total value of your coins

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
