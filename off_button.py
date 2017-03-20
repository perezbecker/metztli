#!/bin/python
#This script was authored by AndrewH7 and belongs to him (www.instructables.com/member/AndrewH7)
#You have permission to modify and use this script only for your own personal usage
#You do not have permission to redistribute this script as your own work
#Use this script at your own risk

import RPi.GPIO as GPIO
import os
import display_X
import time

gpio_pin_number=25
#Replace YOUR_CHOSEN_GPIO_NUMBER_HERE with the GPIO pin number you wish to use
#Make sure you know which rapsberry pi revision you are using first
#The line should look something like this e.g. "gpio_pin_number=7"

GPIO.setmode(GPIO.BCM)
#Use BCM pin numbering (i.e. the GPIO number, not pin number)
#WARNING: this will change between Pi versions
#Check yours first and adjust accordingly

GPIO.setup(gpio_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#It's very important the pin is an input to avoid short-circuits
#The pull-up resistor means the pin is high by default

while True:
    try:
        print "Start routine GPIO INPUT: ", GPIO.input(gpio_pin_number)
        GPIO.wait_for_edge(gpio_pin_number, GPIO.FALLING, timeout=100000)
        print "button pressed or 100s passed, GPIO INPUT: ", GPIO.input(gpio_pin_number)
        #Use falling edge detection to see if pin is pulled
        #low to avoid repeated polling
        #time.sleep(2)
        print "Just Before 2nd test, GPIO INPUT: ", GPIO.input(gpio_pin_number)
        if GPIO.input(gpio_pin_number) == 0:
            print "TEST FAILED, SHUTTING DOWN,GPIO INPUT: ", GPIO.input(gpio_pin_number)

            #display_X.display_X()
            #GPIO.cleanup()
            #Revert all GPIO pins to their normal states (i.e. input = safe)
            #os.system("sudo shutdown -h now")
            #Send command to system to shutdown
        else:
            pass
    except:
        pass
