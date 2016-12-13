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


fullMoon=[[0,0,1,1,1,1,0,0],\
          [0,1,1,1,1,1,1,0],\
          [1,1,1,1,1,1,1,1],\
          [1,1,1,1,1,1,1,1],\
          [1,1,1,1,1,1,1,1],\
          [1,1,1,1,1,1,1,1],\
          [0,1,1,1,1,1,1,0],\
          [0,0,1,1,1,1,0,0]]

halfMoon=[[0,0,1,1,1,1,0,0],\
          [0,1,1,1,1,1,1,0],\
          [1,1,1,1,1,1,0,0],\
          [1,1,1,1,1,1,0,0],\
          [1,1,1,1,1,1,0,0],\
          [1,1,1,1,1,1,0,0],\
          [0,1,1,1,1,1,1,0],\
          [0,0,1,1,1,1,0,0]]


# Run through each pixel individually and turn it on.
display.clear()
for x in range(8):
	for y in range(8):
		# Set pixel at position i, j to on.  To turn off a pixel set
		# the last parameter to 0.
		display.set_pixel(x, y, halfMoon[y][x])
		# Write the display buffer to the hardware.  This must be called to
		# update the actual display LEDs.
display.write_display()
