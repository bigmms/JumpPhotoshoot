import RPi.GPIO as GPIO
import time
PIN_GRE = 32
PIN_YEL = 33
PIN_RED = 31
# 設置為BOARD模式
GPIO.setmode(GPIO.BOARD) 
class LED:
    def __init__(self, pin):
        self.pin = pin
        GPIO.setup(self.pin , GPIO.OUT, initial=GPIO.LOW)

    def on(self):
        # print("ON")
        GPIO.output(self.pin,GPIO.HIGH)

    def off(self):
        # print("OFF")
        GPIO.output(self.pin,GPIO.LOW)

    def __dir__(self):
        GPIO.cleanup()

    def test(self):
        while True:
            time.sleep(1)
            self.on()
            time.sleep(1)
            self.off()
