from rosgraph_msgs.msg import Log

from mavros_msgs.msg import *
from mavros_msgs.srv import *
import rospy

def handle_rosout(data):
    print(f"Received: {data}")

while not rospy.is_shutdown():
    rospy.init_node('arka-2', anonymous=True)
    rate = rospy.Rate(15)
    rospy.Subscriber('/custom', StatusText, handle_rosout)
    rate.sleep()