#!/bin/bash

printop() {
    # WTI 
    w3m -dump https://oilprice.com/ | grep "WTI Crude" | head -n 1
    # print the headline of Newsis realtime news. 
    TOPIN=0
    while read -r line; do
        if [[ $TOPIN == 1 && $line != "" && $line != *"[NISI"* ]]; then
            echo $line | tr -d "\n"
        fi

        if [[ $line == *"[NISI"* ]]; then
            if [[ $TOPIN == 1 ]]; then
                break
            else
                TOPIN=1
            fi
        fi
    done < <(w3m -dump https://www.newsis.com/realnews/)
}

digi_time () {
    dow=""

    case $(date "+%u") in
    1)
        dow="월"
        ;;
    2)
        dow="화"
        ;;
    3)
        dow="수"
        ;;
    4)
        dow="목"
        ;;
    5)
        dow="금"
        ;;
    6)
        dow="토"
        ;;
    7)
        dow="일"
        ;;
    *)
        dow="?"
        ;;
    esac

    echo " $(date "+%y. %m. %d") ${dow}요일          "
    figlet $(date "+%H : %M ${1}") | sed s/\\\\/\\\\\\\\/g | tr " " "\ "
}

chrs=$(echo "$1" | tr -cd '[:alnum:]' | cut -c1-3)

#convert bottom_base$(printf %03d $(($1%5))).png -font ./korean1.ttf -gravity NorthWest +antialias -pointsize 22 -stroke white -fill white -annotate +0+0 "$(printop | grep -oE ".{1,50}")" bottom.png
convert bottom_base003.png -font ./korean1.ttf -gravity NorthWest +antialias -pointsize 22 -stroke white -fill white -annotate +0+0 "$(printop | grep -oE ".{1,50}")" bottom.png
#convert bottom.png -font ./DungGeunMo.ttf -gravity SouthWest +antialias -pointsize 24 -stroke white -fill white -annotate +0+0 "$(digi_time)" bottom.png
convert bottom.png -font ./DungGeunMo.ttf -gravity SouthWest +antialias -pointsize 24 -stroke white -fill white -annotate +0+0 "$(digi_time ${chrs})" bottom.png
convert +transparent white bottom.png bottom.png

