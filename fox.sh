#!/bin/bash

kotit=$(trans -b en:ko "$1" || trans -b en:ko "$1" || trans -b en:ko "$1")

convert fox_base.png -font ./korean1.ttf -gravity North +antialias -pointsize 22 -stroke black -fill black -annotate +0+0 "$(echo $kotit | grep -oE ".{1,50}")" bot_temp.png

