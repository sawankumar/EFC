import machine
import pyb
import framebuf
import time

SCREEN_WIDTH = 64
SCREEN_HEIGHT = 32

# The slider is connected to pin Y4, try adjusting it
adc_pin = machine.Pin('Y4')
adc = pyb.ADC(adc_pin)
adc_value = int(adc.read())

# The pyboard has four simple servo connections
servo = pyb.Servo(1)
servo.angle(adc_value // 3, 500)

# LCD display
i2c = machine.I2C('X')
fbuf = framebuf.FrameBuffer(bytearray(SCREEN_WIDTH * SCREEN_HEIGHT // 8), SCREEN_WIDTH, SCREEN_HEIGHT, framebuf.MONO_HLSB)
fbuf.fill(0)
fbuf.text(str(adc_value), 15, 8)
i2c.writeto(8, fbuf)

# The external LED is connected to our virtual pin Y12
led_pin = machine.Pin('Y12', machine.Pin.OUT)
if adc_value % 2 == 0:
    led_pin.off()  # Switch LED off
else:
    led_pin.on()   # Switch LED on

for i in range(adc_value):
    pyb.LED((i % 4) + 1).toggle()  # Toggle board's built-in LEDs
    time.sleep_ms(50)
