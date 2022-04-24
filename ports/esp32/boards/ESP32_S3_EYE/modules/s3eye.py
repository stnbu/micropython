# ESP32_S3_EYE v2.2 MicroPython Helper Library
# lifted from: https://github.com/espressif/esp32-camera

from micropython import const
from machine import Pin, I2C, Signal
from s3eye_lcd import LCD

# Pin Assignments

# SPI
SPI_MOSI = const(13)
SPI_MISO = const(12)
SPI_CLK = const(14)

# https://github.com/espressif/esp-who/blob/7199eb1619cffbae91f1f0199c6aae9c7ac08dc7/components/screen/test/lcd_mono_test.c#L60
# I2C
I2C_SDA = const(12)
I2C_SCL = const(9)

## the heck are these
# DAC
DAC1 = const(17)
DAC2 = const(18)

# LED
LED = const(3)

# the heck https://github.com/espressif/esp-who/blob/7199eb1619cffbae91f1f0199c6aae9c7ac08dc7/components/modules/lcd/who_lcd.h#L12
# LCD
#LCD_RST = const(-1)
# or is it...
LCD_RST = const(11)

# BUTTON
BUTTON = const(1)

# Helper methods for built in sensors

led = Signal(LED, Pin.OUT, value=0, invert=True)

button = Pin(BUTTON, Pin.IN, Pin.PULL_UP)

i2c = I2C(2)
lcd = LCD(i2c, Pin(LCD_RST))
