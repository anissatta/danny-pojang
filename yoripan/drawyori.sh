#!/bin/sh

digi_time () {
#    figlet $(date "+%H : %M ${1}") | sed s/\\\\/\\\\\\\\/g | tr " " "\ "
    figlet "${1}" | sed s/\\\\/\\\\\\\\/g | tr " " "\ "
}

chrs=$(echo "$1" | tr -cd '[:alnum:]' | cut -c1-3)

#/home/user/danny-pojang/yoripan/yoripan.py > /home/user/danny-pojang/yoripan/core
# execute yoripan-createpan.sh with no arguments so that the news instead will be printed. 
/home/user/danny-pojang/yoripan/yoripan-createpan.sh > /home/user/danny-pojang/yoripan/core
cat /home/user/danny-pojang/yoripan/heada.html /home/user/danny-pojang/yoripan/bg.uri /home/user/danny-pojang/yoripan/headb.html /home/user/danny-pojang/yoripan/core /home/user/danny-pojang/yoripan/tail.html > /home/user/danny-pojang/yoripan/index.html
#wkhtmltoimage --width 800 --crop-h 320 /home/user/danny-pojang/yoripan/index.html /home/user/danny-pojang/yoripan/yori.png
wkhtmltoimage --crop-w 800 --crop-h 320 /home/user/danny-pojang/yoripan/index.html /home/user/danny-pojang/yoripan/yori.png
convert /home/user/danny-pojang/yoripan/yori.png -font ./DungGeunMo.ttf -gravity SouthWest +antialias -pointsize 24 -stroke green -fill white -annotate +0+0 "$(digi_time ${chrs})" /home/user/danny-pojang/yoripan/yori.png

