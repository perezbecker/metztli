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

def displayNumber(CurrentMoon):

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


def fullDisplay(CurrentMoon):

    mm.displayMatrix(CurrentMoon)
    displayNumber(CurrentMoon)

    return

displayNoNumber()
# mm.initpy()
time.sleep(1)

IPstring = subprocess.Popen('./getIPend1.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in IPstring.stdout.readlines():
    IPstringline = line
FIPaddress=int(IPstringline)
displayInteger(FIPaddress)
time.sleep(2)

IPstring = subprocess.Popen('./getIPend2.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in IPstring.stdout.readlines():
    IPstringline = line
FIPaddress=int(IPstringline)
displayInteger(FIPaddress)
time.sleep(2)

IPstring = subprocess.Popen('./getIPend3.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in IPstring.stdout.readlines():
    IPstringline = line
FIPaddress=int(IPstringline)
displayInteger(FIPaddress)
time.sleep(2)

IPstring = subprocess.Popen('./getIPend4.sh', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in IPstring.stdout.readlines():
    IPstringline = line
FIPaddress=int(IPstringline)
displayInteger(FIPaddress)
time.sleep(2)

fullDisplay(0.00)
time.sleep(2)
CurrentMoon=gm.getCurrentMoon()
twoDecCurrentMoon = float("%.2f" % CurrentMoon)

for i in range(int(twoDecCurrentMoon*100.)):
    fullDisplay(float(i)/100.)
    time.sleep(0.001)

# while True:
#     if(int(time.time())%3600 == 0):
#          CurrentMoon=gm.getCurrentMoon()
#          fullDisplay(CurrentMoon)
#     else:
#         time.sleep(0.5)
