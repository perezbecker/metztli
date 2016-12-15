import getMoon as gm
import matrixMoons as mm
import time

from Adafruit_LED_Backpack import SevenSegment


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment(address=0x71)

# Initialize the display. Must be called once before using the display.
display.begin()

# Keep track of the colon being turned on or off.
colon = False

CurrentMoon=gm.getCurrentMoon()

mm.displayMoonCycles(CurrentMoon)
mm.displayMatrix(CurrentMoon)

if(CurrentMoon > 100.):
    CurrentMoon = float("%.1f" % CurrentMoon)
else:
    CurrentMoon = float("%.2f" % CurrentMoon)

# Clear the display buffer.
display.clear()
# Print a floating point number to the display.
if(CurrentMoon < 100.):
    display.print_float(CurrentMoon)
else:
    display.print_float(CurrentMoon, decimal_digits=1)
# Set the colon on or off (True/False).
display.set_colon(colon)
# Write the display buffer to the hardware.  This must be called to
# update the actual display LEDs.
display.write_display()
# Delay for a second.
time.sleep(1.0)
