#!/usr/bin/env python3

import rospy
from gazebo_ros_link_attacher.srv import Attach, AttachRequest, AttachResponse


if __name__ == '__main__':
    rospy.init_node('trash_tray_attach')
    rospy.loginfo("Creating ServiceProxy to /link_attacher_node/attach")
    attach_srv = rospy.ServiceProxy('/link_attacher_node/attach',
                                    Attach)
    attach_srv.wait_for_service()
    rospy.loginfo("Created ServiceProxy to /link_attacher_node/attach")

    # Link them
    # rospy.loginfo("Attaching cube1 and cube2")
    req = AttachRequest()
    req.model_name_1 = "apbot"
    req.link_name_1 = "trash_tray_1"
    req.model_name_2 = "apbot"
    req.link_name_2 = "base_link"

    attach_srv.call(req)