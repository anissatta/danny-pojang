#!/bin/sh

convert /home/user/danny-pojang/right/logo-base.png -font /home/user/danny-pojang/korean1.ttf -gravity NorthWest -pointsize 24 +antialias -fill "white" -annotate +0+0 "$(echo "$1" | grep -oE ".{1,20}")" /home/user/danny-pojang/logo.png
#convert /home/user/danny-pojang/right/logo.png -background "#000" -wave 8x120 /home/user/danny-pojang/right/logo.png

