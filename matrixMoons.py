import time

from PIL import Image
from PIL import ImageDraw

from Adafruit_LED_Backpack import Matrix8x8

# Create display instance on default I2C address (0x70) and bus number.
display = Matrix8x8.Matrix8x8()

# Alternatively, create a display with a specific I2C address and/or bus.
# display = Matrix8x8.Matrix8x8(address=0x74, busnum=1)

# Initialize the display. Must be called once before using the display.
display.begin()

# Set display brightness (15 is max, 0 is min).
display.set_brightness(5)


def displayMatrix(CurrentMoon):

    Moon00=[[0,0,1,1,1,1,0,0],\
            [0,1,1,1,1,1,1,0],\
            [1,1,1,1,1,1,1,1],\
            [1,1,1,1,1,1,1,1],\
            [1,1,1,1,1,1,1,1],\
            [1,1,1,1,1,1,1,1],\
            [0,1,1,1,1,1,1,0],\
            [0,0,1,1,1,1,0,0]]

    Moon01=[[0,0,1,1,1,1,0,0],\
            [0,1,1,1,1,1,1,0],\
            [1,1,1,1,1,1,1,0],\
            [1,1,1,1,1,1,1,0],\
            [1,1,1,1,1,1,1,0],\
            [1,1,1,1,1,1,1,0],\
            [0,1,1,1,1,1,1,0],\
            [0,0,1,1,1,1,0,0]]

    Moon02=[[0,0,1,1,1,0,0,0],\
            [0,1,1,1,1,1,0,0],\
            [1,1,1,1,1,1,0,0],\
            [1,1,1,1,1,1,0,0],\
            [1,1,1,1,1,1,0,0],\
            [1,1,1,1,1,1,0,0],\
            [0,1,1,1,1,1,0,0],\
            [0,0,1,1,1,0,0,0]]

    Moon03=[[0,0,1,1,0,0,0,0],\
            [0,1,1,1,1,0,0,0],\
            [1,1,1,1,1,0,0,0],\
            [1,1,1,1,1,0,0,0],\
            [1,1,1,1,1,0,0,0],\
            [1,1,1,1,1,0,0,0],\
            [0,1,1,1,1,0,0,0],\
            [0,0,1,1,0,0,0,0]]

    Moon04=[[0,0,1,1,0,0,0,0],\
            [0,1,1,1,0,0,0,0],\
            [1,1,1,1,0,0,0,0],\
            [1,1,1,1,0,0,0,0],\
            [1,1,1,1,0,0,0,0],\
            [1,1,1,1,0,0,0,0],\
            [0,1,1,1,0,0,0,0],\
            [0,0,1,1,0,0,0,0]]

    Moon05=[[0,0,1,1,0,0,0,0],\
            [0,1,1,0,0,0,0,0],\
            [1,1,1,0,0,0,0,0],\
            [1,1,1,0,0,0,0,0],\
            [1,1,1,0,0,0,0,0],\
            [1,1,1,0,0,0,0,0],\
            [0,1,1,0,0,0,0,0],\
            [0,0,1,1,0,0,0,0]]

    Moon06=[[0,0,1,0,0,0,0,0],\
            [0,1,0,0,0,0,0,0],\
            [1,1,0,0,0,0,0,0],\
            [1,1,0,0,0,0,0,0],\
            [1,1,0,0,0,0,0,0],\
            [1,1,0,0,0,0,0,0],\
            [0,1,0,0,0,0,0,0],\
            [0,0,1,0,0,0,0,0]]

    Moon07=[[0,0,1,0,0,0,0,0],\
            [0,1,0,0,0,0,0,0],\
            [1,0,0,0,0,0,0,0],\
            [1,0,0,0,0,0,0,0],\
            [1,0,0,0,0,0,0,0],\
            [1,0,0,0,0,0,0,0],\
            [0,1,0,0,0,0,0,0],\
            [0,0,1,0,0,0,0,0]]

    Moon08=[[0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0],\
            [0,0,0,0,0,0,0,0]]

    Moon09=[[0,0,0,0,0,1,0,0],\
            [0,0,0,0,0,0,1,0],\
            [0,0,0,0,0,0,0,1],\
            [0,0,0,0,0,0,0,1],\
            [0,0,0,0,0,0,0,1],\
            [0,0,0,0,0,0,0,1],\
            [0,0,0,0,0,0,1,0],\
            [0,0,0,0,0,1,0,0]]

    Moon10=[[0,0,0,0,0,1,0,0],\
            [0,0,0,0,0,0,1,0],\
            [0,0,0,0,0,0,1,1],\
            [0,0,0,0,0,0,1,1],\
            [0,0,0,0,0,0,1,1],\
            [0,0,0,0,0,0,1,1],\
            [0,0,0,0,0,0,1,0],\
            [0,0,0,0,0,1,0,0]]

    Moon11=[[0,0,0,0,1,1,0,0],\
            [0,0,0,0,0,1,1,0],\
            [0,0,0,0,0,1,1,1],\
            [0,0,0,0,0,1,1,1],\
            [0,0,0,0,0,1,1,1],\
            [0,0,0,0,0,1,1,1],\
            [0,0,0,0,0,1,1,0],\
            [0,0,0,0,1,1,0,0]]

    Moon12=[[0,0,0,0,1,1,0,0],\
            [0,0,0,0,1,1,1,0],\
            [0,0,0,0,1,1,1,1],\
            [0,0,0,0,1,1,1,1],\
            [0,0,0,0,1,1,1,1],\
            [0,0,0,0,1,1,1,1],\
            [0,0,0,0,1,1,1,0],\
            [0,0,0,0,1,1,0,0]]

    Moon13=[[0,0,0,0,1,1,0,0],\
            [0,0,0,1,1,1,1,0],\
            [0,0,0,1,1,1,1,1],\
            [0,0,0,1,1,1,1,1],\
            [0,0,0,1,1,1,1,1],\
            [0,0,0,1,1,1,1,1],\
            [0,0,0,1,1,1,1,0],\
            [0,0,0,0,1,1,0,0]]

    Moon14=[[0,0,0,1,1,1,0,0],\
            [0,0,1,1,1,1,1,0],\
            [0,0,1,1,1,1,1,1],\
            [0,0,1,1,1,1,1,1],\
            [0,0,1,1,1,1,1,1],\
            [0,0,1,1,1,1,1,1],\
            [0,0,1,1,1,1,1,0],\
            [0,0,0,1,1,1,0,0]]

    Moon15=[[0,0,1,1,1,1,0,0],\
            [0,1,1,1,1,1,1,0],\
            [0,1,1,1,1,1,1,1],\
            [0,1,1,1,1,1,1,1],\
            [0,1,1,1,1,1,1,1],\
            [0,1,1,1,1,1,1,1],\
            [0,1,1,1,1,1,1,0],\
            [0,0,1,1,1,1,0,0]]

    MoonErr=[[1,0,0,0,0,0,0,1],\
            [0,1,0,0,0,0,1,0],\
            [0,0,1,0,0,1,0,0],\
            [0,0,0,1,1,0,0,0],\
            [0,0,0,1,1,0,0,0],\
            [0,0,1,0,0,1,0,0],\
            [0,1,0,0,0,0,1,0],\
            [1,0,0,0,0,0,0,1]]

    CurrentMoonFraction=CurrentMoon-int(CurrentMoon)

    if(CurrentMoonFraction >= 0.96875 or CurrentMoonFraction < 0.03125):
        MMoon=Moon00
    elif(CurrentMoonFraction >= 0.03125 and CurrentMoonFraction < 0.09375):
        MMoon=Moon01
    elif(CurrentMoonFraction >= 0.09375 and CurrentMoonFraction < 0.15625):
        MMoon=Moon02
    elif(CurrentMoonFraction >= 0.15625 and CurrentMoonFraction < 0.21875):
        MMoon=Moon03
    elif(CurrentMoonFraction >= 0.21875 and CurrentMoonFraction < 0.28125):
        MMoon=Moon04
    elif(CurrentMoonFraction >= 0.28125 and CurrentMoonFraction < 0.34375):
        MMoon=Moon05
    elif(CurrentMoonFraction >= 0.34375 and CurrentMoonFraction < 0.40625):
        MMoon=Moon06
    elif(CurrentMoonFraction >= 0.40625 and CurrentMoonFraction < 0.46875):
        MMoon=Moon07
    elif(CurrentMoonFraction >= 0.46875 and CurrentMoonFraction < 0.53125):
        MMoon=Moon08
    elif(CurrentMoonFraction >= 0.53125 and CurrentMoonFraction < 0.59375):
        MMoon=Moon09
    elif(CurrentMoonFraction >= 0.59375 and CurrentMoonFraction < 0.65625):
        MMoon=Moon10
    elif(CurrentMoonFraction >= 0.65625 and CurrentMoonFraction < 0.71875):
        MMoon=Moon11
    elif(CurrentMoonFraction >= 0.71875 and CurrentMoonFraction < 0.78125):
        MMoon=Moon12
    elif(CurrentMoonFraction >= 0.78125 and CurrentMoonFraction < 0.84375):
        MMoon=Moon13
    elif(CurrentMoonFraction >= 0.84375 and CurrentMoonFraction < 0.90625):
        MMoon=Moon14
    elif(CurrentMoonFraction >= 0.90625 and CurrentMoonFraction < 0.96875):
        MMoon=Moon15
    else:
        MMoon=MoonErr


    display.clear()
    for x in range(8):
    	for y in range(8):
    		# Set pixel at position i, j to on.  To turn off a pixel set
    		# the last parameter to 0.
    		display.set_pixel(x, y, MMoon[y][x])
    		# Write the display buffer to the hardware.  This must be called to
    		# update the actual display LEDs.
    display.write_display()

    return

def initpy():
	# Run through each pixel individually and turn it on.
	for x in range(8):
		for y in range(8):
			# Clear the display buffer.
			display.clear()
			# Set pixel at position i, j to on.  To turn off a pixel set
			# the last parameter to 0.
			display.set_pixel(y, x, 1)
			# Write the display buffer to the hardware.  This must be called to
			# update the actual display LEDs.
			display.write_display()
			# Delay for half a second.
			time.sleep(0.5)

    return
