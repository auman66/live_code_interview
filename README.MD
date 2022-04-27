# Prerequisites

- [ROS Noetic](http://wiki.ros.org/noetic/Installation/Ubuntu)
- [Catkin](https://catkin-tools.readthedocs.io/en/latest/installing.html)
- [Gazebo](https://classic.gazebosim.org/tutorials?tut=ros_installing&cat=connect_ros)
- [Turtlesim](http://wiki.ros.org/turtlesim)
- [Turtlebot](https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/)

# Set Up

1. Grab turlebot sim:
```
$ cd ~/catkin_ws/source
$ git clone -b noetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
```
2. Follow tutorial for [Installing and Configuring Your ROS Environment](http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment)

3. Create Package (see [Creating a ROS Package](http://wiki.ros.org/ROS/Tutorials/CreatingPackage) tutorial):
```
$ catkin_create_pkg live_code std_msgs rospy roscpp geometry_msgs rostime
```

4. Add scripts folder
```
$ mkdir live_code/scripts
```

5. Create file named `move.py` in scripts folder

6. Add `move.py` to cmake by uncommenting lines and adding:
```
catkin_install_python(PROGRAMS
  scripts/move.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```
6. Build
```
$ cd ~/catkin_ws
$ catkin build
```

7. Source
```
$ source devel/setup.bash
```
**Note:** Adding `source ~/catkin_ws/devel/setup.bash` to your `~/.bashrc` file is a good shortcut for this

# Running the system
## Running turtlesim
```
$ rosrun turtlesim turtlesim_node
$ rosrun rosrun live_code move_bot.py
```

## Running turtlebot simulation
```
$ export TURTLEBOT3_MODEL=burger
$ roslaunch turtlebot3_gazebo turtlebot3_house.launch
$ rosrun live_code move_bot.py
```

**Note:** Don't forget to run `roscore` first

Helpful Sources:
- [ROS Tutorials](http://wiki.ros.org/ROS/Tutorials)
- [Turltebot 3 simulation setup](https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation)