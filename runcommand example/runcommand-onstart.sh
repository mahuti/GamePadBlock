#!/usr/bin/env bash

# get the system name argument
sys=$1

# Pass argument along to gamepadblock script
sudo python /home/pi/gamepadblock/launch-gamepadblock.py "$sys"