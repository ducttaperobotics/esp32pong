# This is a demo for driving a SPI black and white 128 x 64 screen
# The board has both SPI and I2C connectors, we

from machine import Pin, SPI
import sh1106

# SPI bus — VSPI pins
spi = SPI(2, baudrate=1000000,
          sck=Pin(18), mosi=Pin(23))

# sh1106.SH1106_SPI(width, height, spi, dc, res, cs)
oled = sh1106.SH1106_SPI(128, 64, spi,
                         dc=Pin(16), res=Pin(17), cs=Pin(5))

oled.fill(0)
oled.text("Hello,", 0, 10)
oled.text("ESP32!", 0, 30)
oled.text("MicroPython", 0, 50)
oled.show()
