Puppycam
========

A Raspberry Pi project to enable me to keep an eye on my dog at home while I'm at work. It consists of a shell script that snaps pictures from a webcam connected via USB, and a Flask website (forwarded via [FreeDNS](http://freedns.afraid.org)) to view the pictures remotely. The shell script runs every 10 minutes from 8am to 7pm via a cron job, added to the system crontab like so:

    */10 8-18 * * 1-5 root /etc/cron.d/puppycam.sh > /dev/null
