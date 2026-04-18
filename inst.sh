#!/bin/bash

sudo apt-get update
sudo apt-get install python3-venv pip gawk
sudo apt-get install ffmpeg gnuplot qiv
sudo apt-get install imagemagick figlet
sudo apt-get install wget w3m pup
wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-3/wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
sudo apt install ./wkhtmltox_0.12.6.1-3.bookworm_amd64.deb
cd /home/user
python3 -m venv py
source py/bin/activate
pip install kiwipiepy
wget git.io/trans
chmod +x ./trans
