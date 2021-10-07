#!/bin/bash

echo "ROS melodic install and setting shell script for Nvidia Jetson Devices"
echo "The script runs in 5 seconds. Press CLTL+C to cancel."
sleep 5s
echo
echo

echo "Timezone Setting"
sudo timedatectl set-timezone 'Asia/Seoul'
sudo timedatectl

sudo hostnamectl set-hostname ros-jetson

sudo apt update && sudo apt dist-upgrade -y && sudo apt autoremove -y
sudo apt install net-tools ssh nmap htop vim git nload software-properties-common \
    wget gzip glances curl build-essential apt-transport-https python3 gnupg2 lsb-release terminator \
    xorg xrdp xserver-xorg mesa-utils xauth gdm3 htop -y
sudo apt-get remove --purge libreoffice* -y
sudo apt clean && sudo apt autoremove -y

echo
echo
echo "check arch"
echo $(dpkg --print-architecture)

echo
echo
echo "OpenCR Board USB Port Settings"
wget https://raw.githubusercontent.com/ROBOTIS-GIT/OpenCR/master/99-opencr-cdc.rules
sudo cp ./99-opencr-cdc.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules
sudo udevadm trigger
sudo chmod a+rw /dev/ttyACM0

echo
echo
echo "ROS melodic Install...."
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update && sudo apt dist-upgrade -y
sudo apt install python-rosdep python-rosinstall-generator python-wstool python-rosinstall cmake chrony ntpdate -y
sudo apt install python-catkin-tools ros-melodic-rosserial-arduino ros-melodic-rosserial-python ros-melodic-hls-lfcd-lds-driver ros-melodic-joy \
    ros-melodic-dynamixel-sdk ros-melodic-ros-base ros-melodic-desktop-full -y 

echo "Setup 2GB Swap Partition"
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
sudo sh -c "echo \"/swapfile swap swap defaults 0 0\" >> /etc/fstab"

sudo rosdep init
rosdep update
mkdir -p ~/catkin_ws
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git ~/catkin_ws/src/turtlebot3
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git ~/catkin_ws/src/turtlebot3
git clone -b melodic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git ~/catkin_ws/src/turtlebot3_msgs
cd ~/catkin_ws && catkin_make
source /opt/ros/melodic/setup.bash
source ~/catkin_ws/devel/setup.bash 
echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

echo
echo
echo "RPLIDAR A2 install"
git clone https://github.com/Slamtec/rplidar_ros ~/catkin_ws/src/rplidar_ros
cd ~/catkin_ws && catkin_make
mv ~/turtlebot3_lidar.launch ~/catkin_ws/src/turtlebot3/turtlebot3_bringup/launch/

echo
echo
echo "Intel® RealSense™ SDK 2.0 install"
sudo apt-key adv --keyserver keys.gnupg.net --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE || sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-key F6E65AC044F831AC80A06380C8B3A55A6F3EFCDE
sudo add-apt-repository "deb https://librealsense.intel.com/Debian/apt-repo bionic main" -u
sudo apt update 
sudo apt install librealsense2-udev-rules librealsense2	librealsense2-gl librealsense2-net ros-melodic-realsense2-camera -y 

"""
echo
echo
echo "Intel RealSense Install and build"
sudo apt clean && sudo apt autoclean -y
sudo apt update && sudo apt upgrade -y && sudo apt dist-upgrade && sudo apt autoremove -y
sudo apt install libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev -y

echo
echo
# Download the complete source tree with git
git clone https://github.com/IntelRealSense/librealsense.git /tmp/librealsense
mkdir -p /tmp/librealsense/build && cd /tmp/librealsense/build
cmake ..
make -j$(cat /proc/cpuinfo | grep processor | wc -l)
sudo make install

echo
echo
echo "OPENCV 4.2.0 install"
sudo apt update && sudo apt upgrade -y
sudo apt install pkg-config libjpeg-dev libtiff5-dev libpng-dev libavcodec-dev libavformat-dev libswscale-dev libxvidcore-dev libx264-dev libxine2-dev \ 
libv4l-dev v4l-utils libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgtk2.0-dev mesa-utils libgl1-mesa-dri libgtkgl2.0-dev libgtkglext1-dev \
    libatlas-base-dev gfortran libeigen3-dev python2.7-dev python3-dev python-numpy python3-numpy

mkdir -p /tmp/opencv
cd /tmp/opencv
wget -O opencv.zip https://github.com/opencv/opencv/archive/4.2.0.zip
wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.2.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
cd opencv-4.2.0
mkdir build
cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE \
    -D CMAKE_INSTALL_PREFIX=/usr/local \
    -D WITH_TBB=OFF \
    -D WITH_IPP=OFF \
    -D WITH_1394=OFF \
    -D BUILD_WITH_DEBUG_INFO=OFF \
    -D BUILD_DOCS=OFF \
    -D INSTALL_C_EXAMPLES=ON \
    -D INSTALL_PYTHON_EXAMPLES=ON \
    -D BUILD_EXAMPLES=OFF \
    -D BUILD_TESTS=OFF \
    -D BUILD_PERF_TESTS=OFF \
    -D WITH_QT=OFF \
    -D WITH_GTK=ON \
    -D WITH_OPENGL=ON \
    -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.2.0/modules \
    -D WITH_V4L=ON \
    -D WITH_FFMPEG=ON \
    -D WITH_XINE=ON \
    -D BUILD_NEW_PYTHON_SUPPORT=ON \
    -D OPENCV_GENERATE_PKGCONFIG=ON ../

time make -j$(cat /proc/cpuinfo | grep processor | wc -l)
sudo make install

echo
echo
echo "/etc/ld.so.conf.d/ 디렉토리에 /usr/local/lib 포함하는 설정파일이 있는지 확인"
cat /etc/ld.so.conf.d/*
sleep 5

echo
echo
sudo apt-get install python3-pip python-catkin-tools python3-dev python3-numpy -y
sudo pip3 install rospkg catkin_pkg
mkdir -p ~/catkin_cvbridge/src
cd ~/catkin_cvbridge/src
git clone -b noetic https://github.com/ros-perception/vision_opencv.git
sed -i 's/find_package(Boost REQUIRED python37)/find_package(Boost REQUIRED python3)/g' ~/catkin_cvbridge/src/vision_opencv/cv_bridge/CMakeLists.txt

cd ~/catkin_cvbridge
catkin config -DPYTHON_EXECUTABLE=/usr/bin/python3 -DPYTHON_INCLUDE_DIR=/usr/include/python3.6m -DPYTHON_LIBRARY=/usr/lib/aarch64-linux-gnu/libpython3.6m.so
catkin config --install
catkin build cv_brige

echo "source ~/catkin_cvbridge/install/setup.bash" >> ~/.bahsrc
source ~/.bahsrc

sudo apt install ros-melodic-ddynamic-reconfigure -y
mkdir -p ~/catkin_realsense/src
cd ~/catkin_realsense/src
git clone https://github.com/IntelRealSense/realsense-ros.git
cd realsense-ros/

catkin_init_workspace
cd ..
catkin_make clean
catkin_make -DCATKIN_ENABLE_TESTING=False -DCMAKE_BUILD_TYPE=Release
catkin_make install
"""

echo "The system reboot in 5 seconds."
sleep 5s
sudo reboot