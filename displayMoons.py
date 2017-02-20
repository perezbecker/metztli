import getMoon as gm
import matrixMoons as mm
import time
import subprocess

from Adafruit_LED_Backpack import SevenSegment


# Create display instance on default I2C address (0x70) and bus number.
display = SevenSegment.SevenSegment(address=0x71)

# Initialize the display. Must be called once before using the display.
display.begin()

def displayNoNumber():
    display.clear()
    display.write_display()
    return

def displayNumber(CurrentMoon,daylight):

    if(CurrentMoon > 100.):
        CurrentMoon = float("%.1f" % CurrentMoon)
    else:
        CurrentMoon = float("%.2f" % CurrentMoon)

    # Clear the display buffer.
    display.clear()

    if(daylight==1):
        display.set_brightness(5)
    else:
        display.set_brightness(0)

    # Print a floating point number to the display.
    if(CurrentMoon < 100.):
        display.print_float(CurrentMoon)
    else:
        display.print_float(CurrentMoon, decimal_digits=1)
    # Set the colon on or off (True/False).
    colon = False
    display.set_colon(colon)
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()

    return


def displayInteger(InputInt):
    # Clear the display buffer.
    display.clear()

    display.print_float(InputInt,decimal_digits=0)
    # Set the colon on or off (True/False).
    colon = False
    display.set_colon(colon)
    # Write the display buffer to the hardware.  This must be called to
    # update the actual display LEDs.
    display.write_display()

    return


def fullDisplay(CurrentMoon,daylight):

    mm.displayMatrix(CurrentMoon,daylight)
    displayNumber(CurrentMoon,daylight)

    return


CurrentMoon,daylight = gm.getCurrentMoon()
fullDisplay(CurrentMoon,daylight)
