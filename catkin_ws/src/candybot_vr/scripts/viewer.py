#!/usr/bin/env python3
'''Allows to view from camera and detect face and smile'''
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')


import rospy
import cv2
from PIL import Image
import io
import argparse
from candybot_vr.vision.algorithmia import facial
'''
DO NOT DELETE 2 NEXT LINES PLEASE - IT IS FOR DEBUGGING AND TEST
sys.path.insert(0,'..')
from src.candybot_vr.vision.algorithmia import facial
'''
import time
import json
import logging
logging.basicConfig(filename='viewer.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

def raw_img2png(raw_img):
    fp = io.BytesIO()
    img = Image.fromarray(raw_img)
    img.save(fp=fp, format='png')
    fp.seek(0)
    return fp
    

def main():
    '''Main function
    Args:
        min_neighbors: minimal face number
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
                    fp = raw_img2png(frame)
                    time_split = time.ctime().split()
                    date = ' '.join(time_split[0:2])
                    write_time = time_split[3]
                    date += ' ' + time_split[len(time_split) - 1]
                    with open('view_stat ' + date,'a') as statf:
                        data = dict()
                        data['time'] = write_time
                        data['emotions'] = facial.get_emotions(fp)
                        fp.seek(0)
                        data['celebrity_sim'] = facial.celebrities_similarity(fp)
                        fp.seek(0)
                        data['gender'] = facial.gender(fp)
                        fp.seek(0)
                        data['age'] = facial.age(fp)
                        print(data)
                        json.dump(obj=data,fp=statf,ensure_ascii=False,indent=4)
                        

                        
                    '''
                    faces = detector.detect(img=frame)
                    message = VisionMessage()
                    print('vvv', message.face_count, ' ' , message.smile)
                    message.face_count = len(faces)
                    
                    for face in faces:
                        if face.smile:
                            message.smile = True

                    publisher.publish(message)
                    '''
    except Exception as e:        
        logging.error(str(e))
        print(str(e))
    

if __name__ == '__main__':
    main()
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--min_neighbors', dest='min_neighbors')
    args = parser.parse_args()
    '''
    
    
    
