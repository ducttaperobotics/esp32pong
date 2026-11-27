from machine import Pin, SPI
#import sh1106
import ssd1306
spi = SPI(2, baudrate=1000000, sck=Pin(18), mosi=Pin(23))
oled = sh1106.SH1106_SPI(128, 64, spi, dc=Pin(16), res=Pin(17), cs=Pin(5))
print("constructed ok")
