# A feladat lépései
1. A led világítás vezérlése
    - Led pwm-be kapcsolása
    - A kitöltési tényezőtöl függő világítás programozása
      - fill: 0..100: 1 -> alig világít, 100 -> full világít 
2. Áram változtatása
  - Írjuk ki a képernyőre az áram változását ahogy tekerjük a potmétert
  - Meghatározzuk a legkisebb és a legmagasabb áramot
  - Ezt az áramváltozást normáljuk 0 és 100 között
  - A normált változást áttöltjük a fillbe
  - Működtetjük a ledet 
3. A hétszegmenses kijelzőre a kitöltési tényező kiírása
  - beimportáljuk a kijelzőhöz tartozó importot és a kommunikáció importját
  - String segítségével működtetjük a 7 segmentses kijelzőt
  - display printel kiírjuk a %-ot a kijelzőre

# 1. A világítás vezérlés
A megvalósítás kódja:
```py
# LED kódja!
T = 1

#LED beállítása
GPIO.setup(pin, GPIO.OUT)
f = 80 # 50 hertz
fill = 20 # fill 90%
# pwm üzemmód bekapcsolása
pinLed = 18
GPIO.setup(pinLed, GPIO.OUT)
pL = GPIO.PWM(pinLed,f)
pL.start(0)

# potméter kódja!

def normal(min, max, n, i):
    if(i<min):
        return 0
    else:
        return math.floor((i-min)/(max-min)*n)

# 7 segmentses kijelző kódja
try:
    while True:
        u = ina.voltage()
        i = ina.current()
        p = ina.power()
        r = u/i
        fill = normal(iMin, iMax, 100,i)
        pL.ChangeDutyCycle(fill)
        
        print(f"Fill = {fill}% ")
        #tempString = str(temp)[:5].ljust(5,"0")
        
        String = str(1.0*fill)[:5].ljust(5,"0")
        display.print(String)
        time.sleep(0.2)
```