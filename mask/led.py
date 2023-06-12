
import RPi.GPIO as GPIO

import time

 


colors = [0xFF0000, 0xFF0023, 0xFF00FF, 0x0000FF, 0x00FF00, 0x64EB00, 0x4BFB00]

pins = {'pin_R':11, 'pin_G':9, 'pin_B':10}  

 

GPIO.setmode(GPIO.BCM)                                          

for i in pins:

    GPIO.setup(pins[i], GPIO.OUT)   

    GPIO.output(pins[i], GPIO.HIGH) 

 

p_R = GPIO.PWM(pins['pin_R'], 2000)  

p_G = GPIO.PWM(pins['pin_G'], 2000)

p_B = GPIO.PWM(pins['pin_B'], 2000)

 

p_R.start(0)     

p_G.start(0)

p_B.start(0)

 

def map(x, in_min, in_max, out_min, out_max):

    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

 



def setColor(col):   

    R_val = (col & 0x110000) >> 16

    G_val = (col & 0x001100) >> 8

    B_val = (col & 0x000011) >> 0

 

    R_val = map(R_val, 0, 255, 0, 100)

    G_val = map(G_val, 0, 255, 0, 100)

    B_val = map(B_val, 0, 255, 0, 100)

 

    p_R.ChangeDutyCycle(100-R_val)  

    p_G.ChangeDutyCycle(100-G_val)

    p_B.ChangeDutyCycle(100-B_val)

 

try:

    while True:                          

        for col in colors:

            setColor(col)

            time.sleep(1.0)

except KeyboardInterrupt:               

    p_R.stop()

    p_G.stop()

    p_B.stop()

    for i in pins:

        GPIO.output(pins[i], GPIO.HIGH)  

        GPIO.cleanup()
