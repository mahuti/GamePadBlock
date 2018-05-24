# GamePadBlock
Utility to dynamically switch the GamePadBlock's mode using the COM port on the Raspberry Pi

GamePadBlock is a piece of hardware that allows you to switch between controllers dynamically and use 2 of each controller. 
For more: https://blog.petrockblock.com/gamepadblock/

This script requires that Pyserial, USB HID Quirks be installed. Instructions for doing this can be found below. 

Also, please note, you will probably still have to only leave the controllers you're using currently plugged in at any one time. If you have two types of controllers that use the same connection method (Sega Genesis controllers and Atari controllers) only one set will work at a time. This is presently a limitation of the GamePadBlock, not the script. 

## Update firmware for GamePadBlock to 1.2+
GamePadBlock must be at firmware 1.2 or greater to dynamically change via the COM port. 
See here for instructions: https://github.com/petrockblog/petrockutil

## Download GamePadBlock Binary
Download the precompiled binary for your specific system from here and copy it to a folder on your Pi named "gamepadblock" in /home/pi/: https://blog.petrockblock.com/gamepadblock-downloads/

*NOTE:* Don't bother doing a custom compile, just get the binaries. If you really want to try compiling it yourself, you can get he source here: 

	git clone --depth 1 https://github.com/petrockblog/petrockutil/ petrockutil-linux-arm 

In my experience, it did not compile on my system because I was missing the needed dependencies.

## Install USB Hid Quirks
So that you can use two of the same gamepads on one port, install USB HID Quirks

	wget -O - https://raw.githubusercontent.com/petrockblog/GamepadBlockScripts/master/gamepadblockRaspbian.sh | sudo bash

## Install Pyserial 
To run this python script for GamePadBlock, install Pyserial

	sudo apt-get install -y python-pip
	sudo pip install pyserial

See this URL for more information if interested: [https://blog.petrockblock.com/2017/11/11/using-virtual-com-port-gamepadblock/]

## Get the location of the GamePadBlock COM Port
You'll need the location of device's COM port (/dev/ttyACM0, etc). This will be added to the script in the next step

	cd /home/pi/gamepadblock
	./petrockutil-linux-arm scan serial 

## Add this script 
Once you have the location of the GamePadBlock, add it to this script in the _*port*_ section. Then copy this script to the gamepadblock folder on your Pi (which I mentioned you should create earlier). 

If you need/want to debug, set the debug flag to True, and make sure you have read/write privileges set on /home/pi/gamepadblock/gpblock.log

You can also set the default mode. It's currently set to "arcade", but you can set it to any of the modes found down around line 60 of the script. 

## Modify runcommand-onstart.sh

To use this automatic controller switcher, you'll need to launch it each time you launch an emulator. 
The following example is what my `runcommand-onstart.sh` file found looks like. To add it: 

	sudo pico /opt/retropie/configs/all/runcommand-onstart.sh

Edit the file, and make it look something like this: 

	#!/usr/bin/env bash
	# get the system name argument
	sys=$1
	# Pass argument along to gamepadblock script
	sudo python /home/pi/gamepadblock/launch-gamepadblock.py "$sys"

You may need to add it after any existing commands you already have set up. 
