import rospy
from geometry_msgs.msg import Twist

# Create a function
def circle():
    # Initialize the node
    rospy.init_node('live_code', anonymous=True)
    # Create a publisher
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    # Create a twist message and assign values for moving in a circle
    vel = Twist()
    vel.linear.x = 0.5
    vel.angular.z = 1.5
    # Publish the velocity on repeat
    while not rospy.is_shutdown():
        pub.publish(vel)

if __name__== '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass

# Steps to run: 
# roslaunch turtlebot3_gazebo turtlebot3_house.launch
# rosrun live_code move_bot.py