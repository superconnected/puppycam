#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
BASE=/home/pi/puppycam/website/static/img

raspistill -vf -hf -w 640 -h 480 -o $BASE/full/$DATE.jpg
convert $BASE/full/$DATE.jpg -resize 250x250 $BASE/thumbnails/$DATE.jpg
