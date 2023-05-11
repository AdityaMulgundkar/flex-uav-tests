from rosgraph_msgs.msg import Log

from mavros_msgs.msg import *
from mavros_msgs.srv import *
import rospy

def handle_rosout(data):
    print(f"Recv:{data}")

flag = True

while not rospy.is_shutdown():
    rospy.init_node('setpoint_node', anonymous=True)
    rate = rospy.Rate(15)
    rospy.Subscriber('/mavros/statustext/recv', StatusText, handle_rosout)
    rate.sleep()