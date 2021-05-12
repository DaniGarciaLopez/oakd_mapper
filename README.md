# oakd_mapper

## Installation (tested on Ubuntu 20.04)
### Install ROS
[Install ROS Noetic](http://wiki.ros.org/noetic/Installation/Debian)

Create ROS workspace:
```
mkdir -p ~/oakd_ws/src
```
Include following lines in ~/.bashrc:
```
source /opt/ros/noetic/setup.bash
source ~/oakd_ws/devel/setup.bash
```

### Clone this repository
```
cd ~/oakd_ws/src
git clone --recursive https://github.com/DaniGarciaLopez/oakd_mapper.git
```
### Install additional packages
```
sudo apt install ros-noetic-rtabmap ros-noetic-rtabmap-ros
```
### Install OAK-D driver
```
cd ~
git clone --recursive https://github.com/luxonis/depthai-core.git --branch develop
cd ~/depthai-core
mkdir build
cd build
cmake .. -D BUILD_SHARED_LIBS=ON
cmake --build . --parallel --config Release --target install
```
### Make ROS package
```
cd ~/oakd_ws
catkin_make --cmake-args -D depthai_DIR=~/depthai-core/build/install/lib/cmake/depthai
```
## How to launch a rosbag
### RGB Camera and Depth rosbag
[Download rgb.bag file](https://drive.google.com/file/d/1eGRTldzFjD78PDNfp45HhFvUsY3a7vwb/view?usp=sharing)
```
rosbag play rgb.bag
```
```
rosrun rviz rviz -d ~/oakd_ws/src/oakd_mapper/oakd_mapper/rviz/camera_rgb.rviz
```
### Stereo Camera and Depth rosbag
[Download stereo.bag file](https://drive.google.com/file/d/1IaS7RY4khQtgjTO0QRlQkQHQkgRWROx8/view?usp=sharing
```
rosbag play stereo.bag
```
```
rosrun rviz rviz -d ~/oakd_ws/src/oakd_mapper/oakd_mapper/rviz/camera_stereo.rviz
```

## Test
```
roslaunch oakd_mapper stereo_rgb_nodelet.launch
```
```
roslaunch depthai_examples rgb_stereo_node.launch 
roslaunch depthai_examples stereo_node.launch 
```
```
rosbag record -e "(.*)stereo_publisher(.*)" "(.*)tf_static" "(.*)nodelet_manager/bond"
```
```
roslaunch rtabmap_ros rtabmap.launch \
    rtabmap_args:="--delete_db_on_start" \
    rgb_topic:=/stereo_publisher/color/image \
    depth_topic:=/stereo_publisher/stereo/depth \
    camera_info_topic:=/stereo_publisher/stereo/camera_info \
    frame_id:=/base_link \
    approx_sync:=false
```
