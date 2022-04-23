Yaaay this builds and runs now! d1a9b0b80a2883a843b7ca03fde3798e11a2d5a4

I can run this

```python
from machine import Pin, SPI
from ssd1306 import SSD1306_SPI
width = 128
height = 64
SPI2_HOST = 2  # appears in esp-who/components/modules/lcd/who_lcd.c
hspi = SPI(SPI2_HOST)
dc = Pin(7)
rst = Pin(11)
cs = Pin(8)
display = SSD1306_SPI(width, height, hspi, dc, rst, cs)
```

And nothing breaks. I can call `.text` and `.show` and `poweroff` and `poweron`... but nothing changes.

Lots of mystery numbers need to be figured out in `modules/*.py`. A good reference for that would be the [esp-who driver code](https://github.com/espressif/esp-who/tree/master/components/screen/controller_driver/ssd1306).