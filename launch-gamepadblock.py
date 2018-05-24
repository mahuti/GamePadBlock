#!/usr/bin/env python

### CONFIGURATION ##################################### 

# change to your device's port location if different
port = "/dev/ttyACM0"

# use a supported system's folder name (see switch below for examples)
default_system = "arcade"
 
# Debug logging. set to True to enable log output. False to disable log. Slows down launch by 4s.
debug = False
debugfile = "/home/pi/gamepadblock/gpblock.log"


###################################################  
 
import serial
import sys

if debug:
        import logging
        import time

        
serialPort = serial.Serial(port, baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=1)  # open serial port

serialPort.write("c".encode())  # send c character to get current mode
lastMode = serialPort.read(size=64)  # read up to 64 bytes. Timeout after 1 second as set above.

if debug:
        logger = logging.getLogger('gpblock.log')
        hdlr = logging.FileHandler(debugfile)
        formatter = logging.Formatter('%(message)s')
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(logging.INFO)

        logger.info("--------- " + time.strftime("%m/%d/%Y %I:%M:%S %p")  + " ---------------")
	    logger.info("last controller mode was " + str(lastMode))



system = sys.argv[1]

def zero():
    serialPort.write("0".encode())

def one():
    serialPort.write("1".encode())

def two():
    serialPort.write("2".encode())

def three():
    serialPort.write("3".encode())

mode = serialPort.read(size=64)

switch = {
        "arcade"        : zero,
        "mame"          : zero,
        "mame4all"      : zero,
        "mame-libretro" : zero,
        "mame-advmame"  : zero,
        "fba"           : zero, 
        "neogeo"        : zero,
        "snes"          : one,
        "nes"           : two,
        "atari2600"     : three,
        "atari7800"     : three,
        "atari800"      : three,
        "atari5200"     : three, 
        "c64"           : three, 
        "c128"          : three, 
        "genesis"       : three, 
        "megadrive"     : three, 
        "mastersystem"  : three, 
        "amiga"         : three, 
        "vc20"          : three, 
}

if system in switch:
     switch[system]()
else: 
    switch[default_system]()

serialPort.close()  # close serial port


if debug:
    time.sleep(4) #timeout, because it takes awhile for port to clear out

	serialPort = serial.Serial(port, baudrate=115200, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=1)  # open serial port again
	serialPort.write("c".encode())
	currentMode = serialPort.read(size=64)

    logger.info("current controller mode is " + str(currentMode))
	serialPort.close()  # close serial port
       



