#!/usr/bin/env python3
'''Allows to view from camera and detect face and smile'''
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')


import rospy
import cv2

logging.basicConfig(filename='viewer.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)
    

def main():
    '''Main function
    '''
    try:
        #set viewing parameter 
        rospy.set_param('viewing', True)
        
        #publisher = rospy.Publisher('vision_decision', VisionMessage, queue_size=1)
        rospy.init_node('viewer', anonymous=True)

        cap = cv2.VideoCapture(0)

        #detector = FaceDetector()
        print('view start')
        while True:
            if rospy.get_param('viewing'):
                ret, frame = cap.read()
                if ret:
                    
                    pass

    except Exception as e:        
        logging.error(str(e))
        print(str(e))
    

if __name__ == '__main__':
    main()
