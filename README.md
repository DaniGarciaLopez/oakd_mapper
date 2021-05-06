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
