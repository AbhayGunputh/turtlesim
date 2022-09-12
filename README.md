# TP ROS TurtleSim

## 1) First, you must create a package in your workspace
## 2) Replace the src file with the src file provided from github
## 3) Steps to run the program

#### i) In one terminal, type:
>     roscore
#### ii) In a second terminal type:
>     rosrun turtlesim
#### iii) In a third terminal type:
>     rosrun turtlesim turtle_teleop_key
#### iv) To add a second turtle, type:
>     rosservice call /spawn [double tab]
>     then type the name of the 2nd turtle
>     press enter after typing the name of the turtle
#### v) To control the second turtle, type:
>     rosrun turtlesim turtle_teleop_key /turtle1/cmd_vel:=/turtle2/cmd_vel


## To run the Node
#### Open a terminal, go to the directory there the package is and type:
>     source deve/setup.bash
#### to run the node, type:
>     rosrun name_of_the_package name_of_the_node
