#!/bin/sh

echo $1
FRS=150
XFRS=168
SKRS=162

annt_msg() {
	convert bot_temp.png -font ./DungGeunMo.ttf -gravity NorthWest -pointsize 24 -stroke pink -annotate +132+16 "$1" bot_temp.png
}

degree1() {
    case $((${1}%12)) in
    0)
        echo -3
        ;;
    1)
        echo -2
        ;;
    2)
        echo -1
        ;;
    3)
        echo 0
        ;;
    4)
        echo 1
        ;;
    5)
        echo 2
        ;;
    6)
        echo 3
        ;;
    7)
        echo 2
        ;;
    8)
        echo 1
        ;;
    9)
        echo 0
        ;;
    10)
        echo -1
        ;;
    11)
        echo -2
        ;;
    *)
        echo 0
        ;;
    esac
}

degree2() {
    case $((${1}%8)) in
    0)
        echo -0.8
        ;;
    1)
        echo -0.4
        ;;
    2)
        echo -0
        ;;
    3)
        echo 0.4
        ;;
    4)
        echo 0.8
        ;;
    5)
        echo 0.4
        ;;
    6)
        echo 0
        ;;
    7)
        echo -0.4
        ;;
    *)
        echo 0
        ;;
    esac
}

# 26. 3. 25 
#convert bot_temp.png -sepia-tone 90% bot_temp.png
# 26. 3. 27 
convert bot_temp.png -wave 2x32 bot_temp.png

h=$(date +"%k")

#if [ $h -gt 4 ] && [ $h -lt 17 ]; then
#	composite -geometry +8+8 pix/w$(($1%4)).xpm bot_temp.png bot_temp.png
#else
#	composite -geometry +8+8 pix/m$(($1%4)).xpm bot_temp.png bot_temp.png
#fi

# another one. 
cat /home/user/danny-pojang/right/head$(printf %03d $(($1%60))).html /home/user/danny-pojang/right/core /home/user/danny-pojang/right/tail.html > /home/user/danny-pojang/right/index.html 
wkhtmltoimage  --width 1120 --crop-h 480 /home/user/danny-pojang/right/index.html right.png

# food CF: 
#composite -gravity SouthEast -geometry +0+0 cf/fr$(printf %03d $(($1%$FRS))).png bot_temp.png bot_temp.png
#composite -gravity North -geometry +0+250 xcf/n$(printf %03d $(($1%$XFRS))).png right.png right.png

# make semi-transparent 
#convert bot_temp.png -alpha set -channel A -evaluate set 60% bot_temp.png
# 26. 3. 24 
#composite -gravity North -geometry +0+0 www2/s$(printf %03d $((($1+30)%$SKRS))).png bot_temp.png bot_temp.png
./drawdogs.py

# 26. 4. 8 The Slow Glass. S 
mv glass3.png glass4.png
mv glass2.png glass3.png
mv glass1.png glass2.png
mv glass0.png glass1.png
convert -resize 288x162! bot_temp.png glass0.png
# 26. 4. 8 The Slow Glass. E 

# ~~draw "TRANSPARENT" DOGS!!!~~ 
#convert bot_temp.png -background 'rgba(0,0,0,0)' -rotate $(degree1 $1) bot_temp.png
#convert bot_temp.png -transparent white bot_temp.png

# auto-insa :) 
#if [ $h -gt 2 ] && [ $h -lt 8 ]; then
#    annt_msg "안녕하세요?"
#fi
#if [ $h -gt 14 ] && [ $h -lt 20 ]; then
#    annt_msg "안녕히 주무세요, 저의 고양이."
#fi

# make semi-transparent 
convert right.png -alpha set -channel A -evaluate set 60% right.png
# 26. 3. 25 
#composite -gravity SouthEast -geometry +0+0 www/s$(printf %03d $(($1%149))).png right.png right.png
# 26. 3. 27 
composite -gravity SouthEast -geometry +576+162 glass0.png right.png right.png
composite -gravity SouthEast -geometry +576+0 right/logo.png right.png right.png
###
# 26. 4. 8 Making The Slow Glass S 
composite -gravity NorthWest -geometry     +0+0 glass1.png glass-base.png glass.png
composite -gravity NorthWest -geometry   +288+0 glass2.png glass.png glass.png
composite -gravity NorthWest -geometry +288+162 glass3.png glass.png glass.png
composite -gravity NorthWest -geometry   +0+162 glass4.png glass.png glass.png
composite -gravity SouthEast -geometry +0+0 glass.png right.png right.png
# 26. 4. 8 Making The Slow Glass E 
convert right.png -transparent "#000" right.png

# make semi-transparent 
#convert fright.png -alpha set -channel A -evaluate set 60% fright.png

# another one #2. 
cat /home/user/danny-pojang/top/head$(printf %03d $(($1%42))).html /home/user/danny-pojang/top/core /home/user/danny-pojang/top/tail.html > /home/user/danny-pojang/top/index.html 
wkhtmltoimage --zoom 0.5 --width 1920 --crop-h 194 /home/user/danny-pojang/top/index.html top.png
# make semi-transparent 
convert top.png -alpha set -channel A -evaluate set 60% -background 'rgba(0,0,0,0)' -rotate $(degree2 $1) top.png
#convert top.png -transparent "#E95464" top.png

# another one #3.2. 
echo "data:image/png;base64,$(base64 -w 0 bot_temp.png)" > bot_temp.uri
cat /home/user/danny-pojang/left/heada.html ./bot_temp.uri /home/user/danny-pojang/left/headb.html /home/user/danny-pojang/left/core /home/user/danny-pojang/left/tail.html > /home/user/danny-pojang/left/index.html 
wkhtmltoimage --width 800 --crop-h 480 /home/user/danny-pojang/left/index.html left.png

# 26. 4. 10 
./killtonda.sh
composite -gravity South killtonda.png left.png left.png

# make semi-transparent 
convert left.png -alpha set -channel A -evaluate set 70% -background 'rgba(0,0,0,0)' -rotate $(degree1 $1) left.png

# another one #3. 
# 3. 24 : now using food CF as background of the bottom. 
#cat /home/user/danny-pojang/bottom/head.html /home/user/danny-pojang/bottom/core /home/user/danny-pojang/bottom/tail.html > /home/user/danny-pojang/bottom/index.html 
#wkhtmltoimage --width 800 --crop-h 320 /home/user/danny-pojang/bottom/index.html bottom.png
# make semi-transparent 
#convert bottom.png -alpha set -channel A -evaluate set 60% bottom.png
# 26. 3. 24 
#convert bottom.png -transparent "#e0e0c0" bottom.png
# 26. 3. 29 

#./drawbottom.sh $1
#composite -gravity NorthWest -geometry +0+0 bottom.png xcf/_n$(printf %03d $(($1%$XFRS))).png bottom.png

# 26. 4. 10 
./kisa.sh
composite -gravity SouthEast kisa.png yoripan/yori.png yoripan/yori.png
# make transparent. 
convert yoripan/yori.png -alpha set -channel A -evaluate set 70% bottom.png
# to be used on the next turn. 
echo "data:image/png;base64,$(base64 -w 0 xcf/_n$(printf %03d $(($1%$XFRS))).png)" > yoripan/bg.uri

