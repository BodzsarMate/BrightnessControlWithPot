# Steps of the exercise
1. Control the LED lighting
    - Switching Led to pwm
    - Programming the lighting depending on the fill factor
      - fill: 0..100: 1 -> barely lit, 100 -> fully lit 
2. Change the current 
  Plot on the screen the change in current as you turn the potentiometer
  - Determine the minimum and maximum current
  - We normalize this current variation between 0 and 100
  - The normalized variation is converted to the fill
  - We operate the LED
3. displaying the fill factor on the seven-segment display
  - import the display import and the communication import
  - String to operate the 7 segments display
  - display print to print the % on the display

# 1. Lighting control
Implementation code:
```py
# LED code!
T = 1

#LED setting
GPIO.setup(pin, GPIO.OUT)
f = 80 # 50 hertz
fill = 20 # fill 90%
# activate pwm mode
pinLed = 18
GPIO.setup(pinLed, GPIO.OUT)
pL = GPIO.PWM(pinLed,f)
pL.start(0)
```
