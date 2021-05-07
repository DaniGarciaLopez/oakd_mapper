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
## Test
```
roslaunch oakd_mapper stereo_rgb_nodelet.launch
```
```
rosbag record -e "(.*)stereo_publisher(.*)" "(.*)tf_static" "(.*)nodelet_manager/bond"
```
```
roslaunch rtabmap_ros rtabmap.launch \
    rtabmap_args:="--delete_db_on_start" \
    rgb_topic:=/kinect2/qhd/image_color_rect \
    depth_topic:=/kinect2/qhd/image_depth_rect \
    camera_info_topic:=/kinect2/qhd/camera_info \
    approx_sync:=false
```
