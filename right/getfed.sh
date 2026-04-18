#!/bin/sh 

url=$1
tit=$2
lng=$3
kiw=$4
dest=/home/user/danny-pojang/right/core

do_ask() {
	/home/user/danny-pojang/top/tomo.py "$1"
}

do_trans() {
    which trans || echo "trans command is unavailable"
    ret=""
    ret=$(trans -b $1 "$tit" || trans -b $1 "$tit" || trans -b $1 "$tit")
    echo "${ret}"
}

draw_logo() {
    /home/user/danny-pojang/right/drawlogo.sh "$1"
}

draw_btm() {
    /home/user/danny-pojang/yoripan/drawyori.sh "$1"
}

case $lng in
    "en")
        # English
        kor="$(do_trans en:ko)"
        draw_logo "$kor"
        draw_btm "$tit"

        echo '' > $dest
        echo '<p><a id="url" href="#">' >> $dest
        echo $url >> $dest
        echo '</a></p>' >> $dest

        echo '<h3 style="margin: 0;"  class="spfont1">' >> $dest
        echo $tit >> $dest
        echo '</h3>' >> $dest

        echo '<h3 style="margin: 0;"  class="spfont1">' >> $dest
        echo $kor >> $dest
        echo '</h3>' >> $dest

        #echo '<h3 style="margin: 0;" >' >> $dest
        #echo $(do_trans en:ja) >> $dest
        #echo '</h3>' >> $dest

        echo '<h3 style="margin: 0;" >' >> $dest
        echo $(do_ask "$tit") >> $dest
        echo '</h3>' >> $dest
        ;;
    "ko")
        # Korean 
        eng="$(do_trans ko:en)"
        draw_logo "$kiw"
        draw_btm "$eng"

        echo '' > $dest
        echo '<p><a id="url" href="#">' >> $dest
        echo $url >> $dest
        echo '</a></p>' >> $dest

        echo '<h3 style="margin: 0;"  class="spfont1">' >> $dest
        echo $tit >> $dest
        echo '</h3>' >> $dest

        echo '<h3 style="margin: 0;"  class="spfont1">' >> $dest
        echo $eng >> $dest
        echo '</h3>' >> $dest

        #echo '<h3 style="margin: 0;" >' >> $dest
        #echo $(do_trans ko:ja) >> $dest
        #echo '</h3>' >> $dest

        echo '<h3 style="margin: 0;" >' >> $dest
        echo $(do_ask "$eng") >> $dest
        echo '</h3>' >> $dest
        ;;
    *)
        echo "Unexpected language code: $lng"
        ;;
esac

