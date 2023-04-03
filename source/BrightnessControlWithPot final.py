import RPi.GPIO as GPIO
import time
import math
import board
import busio

# 7 szegmenses kijező imort
from adafruit_ht16k33 import segments
# i2c kommunikáció import
i2c = busio.I2C(board.SCL, board.SDA)
# 7 szegment kapcsoat i2c-vel
display = segments.Seg7x4(i2c)
# 7 szemg törlés
display.fill(0)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

T = 1

#LED beállítása
pin = 16
GPIO.setup(pin, GPIO.OUT)
f = 80 # 50 hertz
fill = 20 # fill 90%
# pwm üzemmód bekapcsolása
p = GPIO.PWM(pin, f)


from ina219 import INA219
from ina219 import DeviceRangeError

ina = INA219(shunt_ohms=0.1)
ina.configure()

iMax = 10.99
iMin = 0.5

# LED beállítása
f = 50
T = 1/f
pinLed = 18
GPIO.setup(pinLed, GPIO.OUT)
pL = GPIO.PWM(pinLed,f)
pL.start(0)

def normal(min, max, n, i):
    if(i<min):
        return 0
    else:
        return math.floor((i-min)/(max-min)*n)


# 7 segmentses kijelző működtetése
try:
    while True:
        u = ina.voltage()
        i = ina.current()
        p = ina.power()
        r = u/i
        fill = normal(iMin, iMax, 100,i)
        pL.ChangeDutyCycle(fill)
        
        print(f"Fill = {fill}% ({fill*T*10:.3f}ms)")
        #tempString = str(temp)[:5].ljust(5,"0")
        
        String = str(1.0*fill)[:5].ljust(5,"0")
        display.print(String)
        time.sleep(0.3)

except KeyboardInterrupt:
    print("Pinek lekapcsolva")
    GPIO.cleanup()