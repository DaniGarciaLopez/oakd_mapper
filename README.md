# oakd_mapper

## Installation (tested on Ubuntu 20.04)
[Install ROS2 Foxy](https://docs.ros.org/en/foxy/Installation/Linux-Install-Debians.html)

Don't forget to install colcon:
```
sudo apt install python3-colcon-common-extensions
```
Include following lines in ~/.bashrc:
```
source /opt/ros/foxy/setup.bash
source /usr/share/colcon_cd/function/colcon_cd.sh
export _colcon_cd_root=~/ros2_ws
source ~/ros2_ws/install/setup.bash
```
Create a ROS2 workspace:
```
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
```
Clone the repository:
```
git clone https://github.com/DaniGarciaLopez/oakd_mapper.git
```
Compile packages:
```
cd ~/ros2_ws/
colcon build
```

### Install OAK-D driver
```
cd ~
git clone --recursive https://github.com/luxonis/depthai-core.git --branch develop
cd ~/depthai-core
mkdir build
cd build
cmake .. -D BUILD_SHARED_LIBS=ON
cmake --build . --parallel --config Release --target install`  
cd ~
mkdir -p ros2_ws/src
cd ros2_ws/src
git clone https://github.com/luxonis/depthai-ros.git --branch noetic-devel
git clone https://github.com/luxonis/depthai-ros-examples.git --branch noetic-devel
git clone https://github.com/ros-perception/vision_msgs.git --branch noetic-devel
cd ~/ros_ws
catkin_make --cmake-args -D depthai_DIR=~/depthai-core/build/install/lib/cmake/depthai
```



