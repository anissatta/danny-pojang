#!/bin/sh
#   print_mdjson.sh
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

SERVER_UPTIME=$(uptime -p)
PHOTO_MODTIME=$(stat -c %y snap.jpg)
VIDEO_MODTIME=$(stat -c %y o.mp4)
NUM_PHOTOS=$(ls snaps|wc -l)
MAX_PHOTOS=72
STAT1="[ $(./get-stat1.py) ]"
DEMO1="[ $(./get-demo1.py) ]"

echo "{"
echo "    \"serverUptime\": \"${SERVER_UPTIME}\","
echo "    \"photoLastModification\": \"${PHOTO_MODTIME}\","
echo "    \"videoLastModification\": \"${VIDEO_MODTIME}\","
echo "    \"numberOfUnprocessedPhotos\": ${NUM_PHOTOS},"
echo "    \"numberOfPhotosPerVideo\": ${MAX_PHOTOS},"
# 26. 3. 22 
echo "    \"statistics1\": ${STAT1},"
# 26. 3. 25 
echo "    \"demo1\": ${DEMO1},"
# 26. 3. 28 
echo "    \"demo2\": \"\""
echo "}"

