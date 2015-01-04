Puppycam
========

A Raspberry Pi project to enable me to keep an eye on my dog at home while I'm at work. It consists of a shell script that snaps pictures from an attached Raspberry Pi camera module, a python script that reads the picture directories and generates a simple website (forwarded via [FreeDNS](http://freedns.afraid.org)) to view the pictures remotely. The shell script runs every 10 minutes from 8am to 7pm via a cron job, added to the crontab like so:

    */10 8-18 * * 1-5 pi /home/pi/puppycam/puppycam.sh > /dev/null

There is also a cleanup shell script that deletes pictures that are more than 5 days old, in order to conserve space. I have it running every weekday at 8:05 am via a cron job:

    5 8 * * 1-5 pi /home/pi/puppycam/puppycam_cleanup.sh > /dev/null
