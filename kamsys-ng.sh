#!/bin/sh
#   kamsys.sh 
#   Copyright (C) 2023 anissatta
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

upload_via_ftp () {
    echo "performing a fake-upload for ${fn}, for this is just a demo"
}

# 26. 4. 13 
proc_msg=""
proc_mode=""
if [ "$(($1%20))" -eq "0" ];then
    proc_msg="추가 기사 입하 처리를 실시합니다."
    proc_mode="additional"
fi

kdate () {
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

    echo $(date "+%y. %m. %d ${dow}요일 %H:%M ${proc_msg}")
}

mkdir snaps
mkdir arcs

#while true
#do
    # Update: now I use a webcam instead of a device with IPWebcam installed. 
    # it seems that the webcam I use returns a frame which is too bright just after initialization unless I skip several frames with -S option. 
    ## fetch a photo from a device with IPWebcam installed. 
    #wget http://192.168.xxx.xxx:8080/photoaf.jpg -O snap.jpg
    #fswebcam -d /dev/video0 -r 1920x1080 --jpeg 85 -D 5 -S 8 snap.jpg
    ### heey Yoon stop hacking my computer~ 
    #fswebcam -d /dev/video0 -r 1920x1080 --jpeg 85 -D 5 -S 8 snap.jpg || ./honey.sh

    cp snap-demo.jpg snap.jpg

    # preserve a photo with original resolution for uploading. 
    # 26. 3. 16 
    composite -gravity NorthWest -geometry +0+260 left.png snap.jpg snap-xl.jpg
    # 26. 3. 18 
    #composite -gravity NorthWest -geometry +1600+280 fright.png snap-xl.jpg snap-xl.jpg

    # 26. 3. 17 
    composite -gravity NorthWest -geometry +800+260 right.png snap-xl.jpg snap-xl.jpg
    composite -gravity NorthWest -geometry +0+74 top.png snap-xl.jpg snap-xl.jpg
    # 26. 3. 22 
    composite -gravity SouthWest -geometry +0+0 bottom.png snap-xl.jpg snap-xl.jpg

    # 26. 3. 4 a fake and good pointer. 
#    res=$(./getoneko.py $(($1)))
#    d1=$(echo $res | awk -F ',' '{print $1}' -)
#    d2=$(echo $res | awk -F ',' '{print $2}' -)
#    composite -gravity NorthWest -geometry "+${d1}+${d2}" "pointers/$(printf %03d $(($1%115))).png" snap-xl.jpg snap-xl.jpg
    # 26. 3. 24 
    res=$(./getoneko.py $(($1+3)))
    d1=$(echo $res | awk -F ',' '{print $1}' -)
    d2=$(echo $res | awk -F ',' '{print $2}' -)
    d3=$(echo $res | awk -F ',' '{print $3}' -)
    composite -gravity NorthWest -geometry "+${d1}+${d2}" "img/${d3}" snap-xl.jpg snap-xl.jpg

    cp snap-xl.jpg snap.jpg
    
    convert snap-xl.jpg -font ./korean1.ttf -gravity South -pointsize 50 -stroke black -fill orange -annotate +0+30 "$(kdate)" snap-xl.jpg
    # 26. 3. 15 
    convert snap-xl.jpg -font ./korean1.ttf -gravity North -pointsize 24 -stroke orange -annotate +0+0 "$(./news.py)" snap-xl.jpg
    # upload it. 
    upload_via_ftp snap-xl.jpg

    # resize the photo, add a timestamp, etc. 
    convert snap.jpg -resize x800 snap.jpg
    convert snap.jpg -font ./korean1.ttf -gravity South -pointsize 30 -stroke black -fill orange -annotate +0+30 "$(kdate)" snap.jpg
    # 26. 3. 15 
    convert snap.jpg -font ./korean1.ttf -gravity North -pointsize 22 -stroke orange -annotate +0+0 "$(./news.py)" snap.jpg
    # backup it. 
    cp snap.jpg "snaps/$(date -Iminutes).jpg"

    # if number of backups reaches 72, create a video file from them & upload it. 
    # todo: do this async. 
    if [ $(ls snaps|wc -l) -ge 72 ]; then
        rm o.mp4
        ffmpeg -framerate 10 -pattern_type glob -i 'snaps/*.jpg' -c:v libx264 -pix_fmt yuv420p o.mp4
        # move processed backups to another directory. 
        mv snaps/*.jpg arcs/
        # upload the video. 
        upload_via_ftp o.mp4
    fi

    # generate a JSON file containing some information and upload it. 
    ./print_mdjson.sh > metadata.json
    upload_via_ftp metadata.json

    ### 26. 4. 13 
    if [ "$proc_mode" = "additional" ]; then
        /home/user/danny-pojang/kyungje.py
    fi

#    sleep 291
#done

