#!/usr/bin/env python3

import rospy
import rosgraph
import unittest
import time
import ros_numpy
from sensor_msgs.msg import Image
import sys
sys.path.insert(1, '/usr/local/lib/python3.5/dist-packages')
import cv2
from candybot_v2.msg import FaceFeatures

FINDFACE_ANSWER_TIMEOUT = 30


class TestFindfaceSendImage(unittest.TestCase):

    def test(self):
        global FINDFACE_ANSWER_TIMEOUT

        ros_is_running = True
        vision_facial_nodes_is_running = True

        master_vision_face_tracking = rosgraph.Master('/vision_face_tracking')
        master_vision_face_recognition = rosgraph.Master('/vision_face_recognition')

        try:
            master_vision_face_tracking.lookupNode('/vision_face_tracking')
            master_vision_face_recognition.lookupNode('/vision_face_recognition')
        except ConnectionRefusedError:
            ros_is_running = False
        except rosgraph.masterapi.MasterError:
            vision_facial_nodes_is_running = False

        self.assertEqual(ros_is_running, True)
        self.assertEqual(vision_facial_nodes_is_running, True)

        self.answer_recieved = False

        def callback_findface_answer(data: FaceFeatures):
            if isinstance(data, FaceFeatures):
                self.answer_recieved = True

        answer_reciever_sub = rospy.Subscriber('/vision_face_recognition/face_info', FaceFeatures, callback_findface_answer)

        image_publisher = rospy.Publisher('/vision_camera_capture/image', Image, queue_size=1)
        ndarray_img = cv2.imread('8.jpg')
        img = ros_numpy.msgify(Image, ndarray_img, encoding='rgb8')
        image_publisher.publish(img)

        start = time.time()
        while time.time() - start < FINDFACE_ANSWER_TIMEOUT and self.answer_recieved is False:
            time.sleep(0.1)

        self.assertEqual(self.answer_recieved, True)

        answer_reciever_sub.unregister()
        image_publisher.unregister()


if __name__ == '__main__':
    rospy.init_node('test_findface_pro')
    unittest.main()
