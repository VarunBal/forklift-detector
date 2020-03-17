#!/bin/bash
if [ $# -eq 0 ]
  then
    echo "ERROR! Usage: help/video filepath"
    exit
fi

./darknet detector demo cfg/forklift.data cfg/yolo_custom.cfg backup/train_backup/yolo_custom_final.weights -thresh 0.09 $1 -prefix pictures
avconv -i pictures_%08d.jpg -pix_fmt yuv420p video.mp4
avconv -i video.mp4 -i $1 output.mp4

rm pictures_*.jpg video.mp4