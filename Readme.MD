# Aruco Path Planning Using ROS

## Overview

This project implements path planning using Aruco markers and the Robot Operating System (ROS). The system uses Aruco markers for localization and navigation, allowing a robot to plan and follow a path marked by these visual cues.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Configuration](#configuration)

- [Contributing](#contributing)
- [License](#license)

## Prerequisites
- Ubuntu 20.04 or later
- ROS Humble
- Python 3.8 or later
- OpenCV 4.5 or later (with Aruco module)
- A webcam or other video capture device

## Installation

### 1. Install ROS
Follow the official [ROS installation guide](http://wiki.ros.org/noetic/Installation/Ubuntu) to set up ROS Noetic on your system.

### 2. Install Dependencies
```bash
sudo apt update
sudo apt install pip install cv2 
sudo apt install colcon
```

### 3. Clone the Repository
```bash
git clone https://github.com/DH-ai/Aurco-markers-and-path-planing
cd ~/rrt_assn

```

### 4. Set Up Udev Rules for Camera (Optional)
This ensures your camera is recognized correctly by ROS.
```bash
sudo nano /etc/udev/rules.d/99-usb-camera.rules
```
Add the following line:
```
KERNEL=="video[0-9]*", SUBSYSTEM=="video4linux", ATTR{index}=="0", SYMLINK+="usb_cam"
```
Reload the udev rules:
```bash
sudo udevadm control --reload-rules
sudo udevadm trigger
```

## Usage

### 1. Launch the ROS Nodes
```bash
  colcon build
  source ./install/setup.bash,
ros2 
```
Open a new terminal and run:
```bash
rosrun aruco_path_planning aruco_detector.py
```
Open another terminal and run:
```bash
rosrun aruco_path_planning path_planner.py
```

### 2. Visualize in RViz
To visualize the path planning and marker detection, run:
```bash
rosrun rviz rviz -d ~/catkin_ws/src/aruco_path_planning/rviz/aruco_path_planning.rviz
```

## Features
- **Marker Detection**: Detects Aruco markers in the environment using OpenCV.
- **Localization**: Estimates the robot's position based on the detected markers.
- **Path Planning**: Plans a path using the detected markers as waypoints.
- **Visualization**: Displays the robot's path and markers in RViz.

## Configuration

### Parameters
You can configure various parameters in the `config/config.yaml` file:
- **camera_topic**: The topic name for the camera feed.
- **marker_size**: The size of the Aruco markers in meters.
- **path_tolerance**: Tolerance for path following in meters.

### Launch Files
The `launch/aruco_path_planning.launch` file can be modified to change the nodes and parameters being launched.

## Troubleshooting

### Common Issues
- **Camera not detected**: Ensure the camera is correctly connected and recognized by the system. Check the `/dev` directory for video devices.
- **Markers not detected**: Verify the lighting conditions and ensure the markers are not too small or too far from the camera.
- **RViz not displaying correctly**: Ensure the correct topic names and frames are being used.

### Logs
Check the ROS logs for detailed error messages:
```bash
roslaunch aruco_path_planning aruco_path_planning.launch
```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README to better fit your project's specifics and to add more sections if necessary.
