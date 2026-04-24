#!/bin/bash

# as root, execute this script before starting anything else. 
yes | apt-get update
yes | apt-get install python3-venv pip gawk curl python3-feedparser
yes | apt-get install ffmpeg gnuplot qiv
yes | apt-get install imagemagick figlet
yes | apt-get install wget w3m pup
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
apt install ./wkhtmltox_0.12.6.1-3.bookworm_amd64.deb

