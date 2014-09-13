#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")

fswebcam --no-banner -S 50 /home/pi/puppycam/website/static/img/$DATE.jpg
