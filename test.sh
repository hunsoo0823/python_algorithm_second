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


echo "The system reboot in 5 seconds."
sleep 5s
sudo reboot