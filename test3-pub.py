from rosgraph_msgs.msg import Log

from mavros_msgs.msg import *
from mavros_msgs.srv import *
import rospy

while not rospy.is_shutdown():
    rospy.init_node('arka-1', anonymous=True)
    rate = rospy.Rate(15)
    sp_pub = rospy.Publisher('/custom', StatusText, queue_size=10)

    st = StatusText(text="Ada")
    sp_pub.publish(st)
    print("sent!")
    rate.sleep()