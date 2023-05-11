from rosgraph_msgs.msg import Log

from mavros_msgs.msg import *
from mavros_msgs.srv import *
import rospy

def handle_rosout(data):
    if data.name == '/mavros':
        # handle some info from MAVROS
        if data.msg.startswith('FCU: '):
            print(f"{data.msg}")
        else:
            print(f"OTHER: {data.msg}")

flag = True

while not rospy.is_shutdown():
    rospy.init_node('setpoint_node', anonymous=True)
    rate = rospy.Rate(15)
    rospy.Subscriber('/rosout', Log, handle_rosout)
    sp_pub = rospy.Publisher('/mavros/statustext/send', StatusText, queue_size=10)

    if flag:
        st = StatusText()
        sp_pub.publish(st)
        flag = False
        print("sent!")
    rate.sleep()