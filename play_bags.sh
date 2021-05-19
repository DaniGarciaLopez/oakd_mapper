#!/bin/bash

# Launches oakd bags remapping so it works with rtabmapper 
# demo_stereo_outdoor.launch

gnome-terminal -e "bash -c \"rosbag play --clock stereo.bag \
 /stereo_publisher/left/camera_info:=/stereo_camera/left/camera_info_throttle \
 /stereo_publisher/right/camera_info:=/stereo_camera/right/camera_info_throttle \
 /stereo_publisher/left/image:=/stereo_camera/left/image_rect \
 /stereo_publisher/right/image:=/stereo_camera/right/image_rect \
 /stereo_publisher/stereo/camera_info:=/camera/rgb/camera_info \
 /stereo_publisher/stereo/depth:=/camera/depth_registered/image_raw \""


#gnome-terminal -e "bash -c \"rosbag play --clock rgb.bag \
#/rgb_stereo_publisher/color/camera_info:=/ \
#/rgb_stereo_publisher/color/image:=/ o
#/rgb_stereo_publisher/stereo/camera_info:=/ \
#/rgb_stereo_publisher/stereo/depth:=/ \""