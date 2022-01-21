#! /bin/bash
CURRENT_DEVICES=$(v4l2-ctl --list-devices)
echo $CURRENT_DEVICES
