from pymavlink import mavutil

# Create the connection to the top-side computer as companion computer/autopilot
master = mavutil.mavlink_connection('udpout:localhost:14553', source_system=3, source_component=8)

# Send a message for QGC to read out loud
#  Severity from https://mavlink.io/en/messages/common.html#MAV_SEVERITY
txt = 'Hello World!'
master.mav.statustext_send(mavutil.mavlink.MAV_SEVERITY_NOTICE, txt.encode('utf8'))