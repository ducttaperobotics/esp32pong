from machine import Pin, I2C, ADC
import ssd1306
import time

# --- Screen (I2C) ---
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# --- Joystick ---
xaxis = ADC(Pin(32)); xaxis.atten(ADC.ATTN_11DB)   # 0-3.3V range
yaxis = ADC(Pin(33)); yaxis.atten(ADC.ATTN_11DB)
button = Pin(25, Pin.IN, Pin.PULL_UP)              # pressed = 0

px, py = 64, 32   # dot starts centered

while True:
    x = xaxis.read()      # 0..4095
    y = yaxis.read()

    if x > 3000: px -= 2
    elif x < 1000: px += 2
    if y > 3000: py += 2
    elif y < 1000: py -= 2

    px = max(0, min(127, px))
    py = max(0, min(63, py))

    oled.fill(0)
    oled.fill_rect(px-1, py-1, 3, 3, 1)   # 3x3 dot
    if button.value() == 0:
        oled.text("PRESS", 44, 0)
    oled.show()
    time.sleep(0.02)