#!/bin/sh 

olt_nam=$1
olt_cod=$5
art_url=$2
art_tit=$3
art_lng=$4
dest=/home/user/danny-pojang/top/core

do_ask() {
	/home/user/danny-pojang/top/tomo.py "$1"
}

do_trans() {
    #which trans || echo "trans command is unavailable"
    ret=""
    ret=$(/home/user/trans -b $1 "$art_tit" || trans -b $1 "$art_tit" || trans -b $1 "$art_tit")
    echo "${ret}"
}

echo '' > $dest
echo '<script>' >> $dest
echo "document.getElementById('mybody').className = '${olt_cod}';" >> $dest
echo '</script>' >> $dest

case $art_lng in
    "en")
        # English 
        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans en:ko) >> $dest
        echo '</h3></p>' >> $dest

        #echo '<p><h3>' >> $dest
        #echo $(do_trans en:ja) >> $dest
        #echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_ask "$art_tit") >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "ko")
        # Korean 
        eng="$(do_trans ko:en)"

        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $eng >> $dest
        echo '</h3></p>' >> $dest

        #echo '<p><h3>' >> $dest
        #echo $(do_trans ko:ja) >> $dest
        #echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_ask "$eng") >> $dest
        echo '</h3></p>' >> $dest
        ;;
    "hi") 
        # Hindi 
        eng="$(do_trans hi:en)"

        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans hi:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $eng >> $dest
        echo '</h3></p>' >> $dest

        #echo '<p><h3>' >> $dest
        #echo $(do_trans hi:ja) >> $dest
        #echo '</h3></p>' >> $dest
        ;;
    "ja") 
        # Japanese 
        eng="$(do_trans ja:en)"

        echo '<p><span id="ocd">' >> $dest
        echo $olt_nam >> $dest
        echo '</span></p>' >> $dest

        echo '<p><a id="url" href="#">' >> $dest
        echo $art_url >> $dest
        echo '</a></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $art_tit >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $(do_trans ja:ko) >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3 class="spfont1">' >> $dest
        echo $eng >> $dest
        echo '</h3></p>' >> $dest

        echo '<p><h3>' >> $dest
        echo $(do_ask "$eng") >> $dest
        echo '</h3></p>' >> $dest
        ;;
    *)
        echo "Unexpected language code: $art_lng"
        ;;
esac

