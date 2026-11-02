from machine import Pin
from time import sleep

red_led = Pin(27, Pin.OUT)
yellow_led = Pin(25, Pin.OUT)
green_led = Pin(14, Pin.OUT)


button = Pin(13, Pin.IN, Pin.PULL_DOWN)

print("System Ready! Press the button to change the lights.")


while True:
    
    
    red_led.value(1)
    yellow_led.value(0)
    green_led.value(0)
    
   
    while button.value() == 0:
        sleep(0.01) 
        
   
    while button.value() == 1:
        sleep(0.01)

    # PHASE 2: YELLOW LIGHT
    red_led.value(0)
    yellow_led.value(1)
    green_led.value(0)
    
    # Wait for the next button press
    while button.value() == 0:
        sleep(0.01)
    while button.value() == 1:
        sleep(0.01)

    # PHASE 3: GREEN LIGHT
    red_led.value(0)
    yellow_led.value(0)
    green_led.value(1)
    
    # Wait for the next button press
    while button.value() == 0:
        sleep(0.01)
    while button.value() == 1:
        sleep(0.01)
    
