#!/bin/sh

t=$1

mrprint() {
    echo "(MK 랭킹) " 
    curl -s https://www.mk.co.kr/news/ranking|pup 'div[class="headline"] > span text{}'
}

convert "www/s$(printf %03d $((${t}%149))).png" -font korean1.ttf -gravity NorthWest +antialias -pointsize 21 -stroke white -fill white -annotate +0+0 "$(mrprint | grep -oE ".{1,50}")" www_temp.png

