# oakd_mapper

## Installation (tested on Ubuntu 20.04 with ROS Noetic)
### Install ROS
[Install ROS Noetic](http://wiki.ros.org/noetic/Installation/Debian)

Create ROS workspace:
```
mkdir -p ~/oakd_ws/src
```
Include following lines in ~/.bashrc:
```
source /opt/ros/noetic/setup.bash
source ~/cartographer_ws/install_isolated/setup.bash
source ~/oakd_ws/devel/setup.bash
```

### Clone this repository
```
cd ~/oakd_ws/src
git clone --recursive https://github.com/DaniGarciaLopez/oakd_mapper.git
```
### Install [Google Cartographer](https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html) from source

In order to build Cartographer ROS, we recommend using `wstool` and `rosdep`. For faster builds, we also recommend using `Ninja`.

On Ubuntu Focal with ROS Noetic use these commands to install the above tools:

    sudo apt-get update
    sudo apt-get install -y python3-wstool python3-rosdep ninja-build stow

After the tools are installed, create a new cartographer_ros workspace in 'cartographer_ws'.

    cd ~
    mkdir cartographer_ws
    cd cartographer_ws
    wstool init src
    wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall
    wstool update -t src

Now you need to install ``cartographer_ros`` dependencies.
First, we use ``rosdep`` to install the required packages.
The command 'sudo rosdep init' will print an error if you have already executed it since installing ROS. This error can be ignored.

    sudo rosdep init
    rosdep update
    rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y

Cartographer uses the `abseil-cpp`_ library that needs to be manually installed using this script:

    src/cartographer/scripts/install_abseil.sh 

Due to conflicting versions you might need to uninstall the ROS abseil-cpp using

    sudo apt-get remove ros-${ROS_DISTRO}-abseil-cpp 

Build and install.

    catkin_make_isolated --install --use-ninja
### Install ROS packages
    sudo apt-get install ros-noetic-pointcloud-to-laserscan
### Install OAK-D driver
The following script will install depthai-core and update usb rules and install depthai devices:

```
sudo wget -qO- https://raw.githubusercontent.com/luxonis/depthai-ros/noetic-devel/install_dependencis.sh | bash
```

If you don't have rosdep installed and not initialized please execute the following steps:
1. `sudo apt install python3-rosdep` or `sudo apt install python-rosdep2`(melodic)
2. `sudo rosdep init`
3. `rosdep update`

Install the following vcstool:

`sudo apt install python3-vcstool`

The following setup procedure assumes you have cmake version >= 3.10.2 and OpenCV version >= 4.0.0
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
rosbag play rgb.bag -r 0.5
```
```
rosrun rviz rviz -d ~/oakd_ws/src/oakd_mapper/oakd_mapper/rviz/camera_rgb.rviz
```
### Stereo Camera and Depth rosbag
[Download stereo.bag file](https://drive.google.com/file/d/1IaS7RY4khQtgjTO0QRlQkQHQkgRWROx8/view?usp=sharing)
```
rosbag play --loop stereo.bag --rate 0.5
```
```
rosrun rviz rviz -d ~/oakd_ws/src/oakd_mapper/oakd_mapper/rviz/camera_stereo.rviz
```
### Visualize PointCloud from rosbag
```
rosbag play stereo.bag --loop stereo.bag --rate 0.5 --topics /stereo_publisher/left/image /stereo_publisher/right/image /stereo_publisher/left/camera_info /stereo_publisher/right/camera_info /stereo_publisher/stereo/camera_info /stereo_publisher/stereo/depth

```
```
roslaunch oakd_mapper stereo_nodelet_rosbag.launch
```

## Testing
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
