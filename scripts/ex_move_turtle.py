import rospy
from geometry_msgs.msg import Twist

# Create a function
def circle():
    # Initialize the node
    rospy.init_node('live_code', anonymous=True)
    # Create a publisher
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    # Create a twist message and assign values for moving in a circle
    vel = Twist()
    vel.linear.x = 1
    vel.angular.z = 1
    # Publish the velocity on repeat
    while not rospy.is_shutdown():
        pub.publish(vel)

if __name__== '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass

# rosrun turtlesim turtlesim_node
# rosrun live_code move_turtle.py
