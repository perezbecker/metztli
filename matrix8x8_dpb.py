# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
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
