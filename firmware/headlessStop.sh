#!/bin/bash
sleep 5
kill $(pgrep -f 'python3 recordVideo.py')
#sleep 5
#nohup python3 recordVideo.py > /dev/null 2> /home/teamlary/logs/mqqErr2022.err &

