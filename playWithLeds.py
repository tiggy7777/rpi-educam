# CamJam EduKit 1 - Basics
# Worksheet 2 - LEDs
# Import Libraries
import time # A collection of time related commands
from gpiozero import LED # The LED functions from GPIO Zero
# Set pins 18, 23 and 24 to be LEDs
red = LED(18)
yellow = LED(23)
green = LED(24)


def leds_on():
    print("LEDs on")
    red.on()
    yellow.on()
    green.on()

def leds_off():
    print("LEDs off")
    red.off()
    yellow.off()
    green.off()

for i in range(5):
    leds_on()
    print("Wait for 5 seconds")
    time.sleep(5)
    leds_off()
    time.sleep(5)

