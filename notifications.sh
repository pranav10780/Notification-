#!/bin/bash

# Read the content of bat.txt and store it in a variable
status=$(cat bat.txt)

# Check if the value is "true" or "false"
if [ "$status" = "true" ]; then
    termux-notification --title "BATTERY LEVEL CRITICAL" --content "pls put you phone to charge immediately" --sound --priority high --vibrate 500,1000,500 --led-color FF0000 --icon battery.png;
elif [ "$status" = "false" ]; then
    echo ""
else
    echo "Invalid value in bat.txt"
fi



