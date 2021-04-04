import time
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7789 as st7789
from adafruit_rgb_display.rgb import color565
import adafruit_rgb_display.st7789 as st7789
import webcolors
import re
import adafruit_mpr121


i2c = busio.I2C(board.SCL, board.SDA)

mpr121 = adafruit_mpr121.MPR121(i2c)

# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = None

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=135,
    height=240,
    x_offset=53,
    y_offset=40,
)

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 90

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 26)

# Turn on the backlight
backlight = digitalio.DigitalInOut(board.D22)
backlight.switch_to_output()
backlight.value = True
buttonA = digitalio.DigitalInOut(board.D23)
buttonB = digitalio.DigitalInOut(board.D24)
buttonA.switch_to_input()
buttonB.switch_to_input()

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Main loop:
while True:
    if mpr121[11].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "Song Requested:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "cardigan", font=font, fill="#FFFFFF")
        y += 26
        draw.text((x, y), "Requested by:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Rob", font=font, fill="#FFFFFF")
        y += 26
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight
    
    if mpr121[10].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "Song Requested:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Peaches", font=font, fill="#FFFFFF")
        y += 26
        draw.text((x, y), "Requested by:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Niki", font=font, fill="#FFFFFF")
        y += 26
    
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight

    if mpr121[0].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "DJ Mode:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Self-Select", font=font, fill="#FFFFFF")
        y += 26
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight    

    if mpr121[1].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "DJ Mode:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Rotating", font=font, fill="#FFFFFF")
        y += 26
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight


    if mpr121[2].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "DJ Mode:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Random", font=font, fill="#FFFFFF")
        y += 26
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight

    if mpr121[6].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "Request", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "accepted!", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Song added to", font=font, fill="#FFFFFF")
        y += 26
        draw.text((x, y), "queue.", font=font, fill="#FFFFFF")
        y += 26
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight
    
    if mpr121[8].value:
        backlight.value = True  # turn on backlight
        draw.rectangle((0, 0, width, height), outline=0, fill="#000000")
        y = top
        draw.text((x, y), "Current DJ:", font=font, fill="#1DB954")
        y += 26
        draw.text((x, y), "Ross", font=font, fill="#FFFFFF")
        y += 26
       
        # Display image.
        disp.image(image, rotation)
        time.sleep(1)
    else:
        backlight.value = True  # turn on backlight
        
        

    