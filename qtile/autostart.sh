#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
#wallpaper
xwinwrap -g 1366x768 -ov -ni -- mpv --no-audio -wid WID -loop "/home/juan/Pictures/fondo.mp4" &
#opacity
picom &
