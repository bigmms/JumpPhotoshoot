import time
import LED

class Timer:
    def __init__(self):
        self.endTime = time.time()
        self.strTime = time.time()
        self.oneSecond = 1
        # use GREEN=32 YELLOW=33 RED=31
        self.LED_PIN = (LED.PIN_GRE, LED.PIN_YEL, LED.PIN_RED)
        # all led
        self.ALL_LED = [LED.LED(self.LED_PIN[i]) for i in range(3)]
    
    # start timer
    def start(self):
        self.strTime = time.time()

    # stop timer
    def stop(self):
        self.endTime = time.time()
        return self.endTime - self.strTime
    # 刷新計時器
    def update(self):
        self.endTime = time.time()

    # 是否過了一秒
    def isOneSecond(self):
        if self.endTime - self.strTime > self.oneSecond:
            self.strTime = self.endTime
            return True
        else:
            return False

    # 倒數三秒
    def cntDown(self, camera):
        cnt = 0
        for led in self.ALL_LED:
            led.on()
        while cnt < 3:
            if self.isOneSecond():
                frame = camera.getFrame()
                self.ALL_LED[cnt].off()
                print(cnt)
                cnt += 1

            self.update()

