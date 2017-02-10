#!/usr/bin/env python3
import sys
sys.path.insert(1,'/usr/local/lib/python3.5/dist-packages')

import cv2
import numpy as np
from candybot_vr.vision.opencv.detect_face2 import FaceDetector
import time
import multiprocessing as mpr
import pyaudio
import wave
import os
import logging

logging.basicConfig(filename='write_message.log', format='[%(asctime)s] %(message)s\n\n',
                    level=logging.ERROR)

USERS_FOLDER = 'users'
MSG_DURATION = 30

writing_msg = True

#set of saved faces if person is new
all_saved_faces = list()


def equivalent_faces(face1, face2):
    '''Compares two faces.
    Args:
        face1, face2: faces to compare
    Returns:
        True - if face1 is detected on face2 and vice versa
        False - else
    '''
    
    res = cv2.matchTemplate(face1, face2,cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        return True
    return False
    

def face_already_exists(face):
    '''Uses, where person is new. Filters duplicate faces during its saving
    Args:
        face: person face
    Returns:
        True - if face already exists
        False - else
    '''
    
    for saved_face in all_saved_faces:
        if equivalent_faces(saved_face, face):
            return True
    return False


def find_person(face):
    '''Finds person by face.
    Args:
        face: person face
    Returns:
        person folder path - if person exists
        None - else
    '''
    
    user_folders = os.listdir(USERS_FOLDER)
    for folder in user_folders:
        user_faces = os.listdir('/'.join([USERS_FOLDER,folder,'faces']))
        for user_face in user_faces:
            user_face_img = cv2.imread('/'.join([USERS_FOLDER,
                                                 folder,'faces',user_face]))
            if equivalent_faces(user_face_img, face):
                return '/'.join([USERS_FOLDER,folder])
    return None

def create_new_user_folder():
    '''Creates new user folder.
    New user folder name is 1 greater than users folders number already exists
    Returns:
        new user folder path
    '''
    
    new_user_folder =  str(len(os.listdir(USERS_FOLDER)) + 1)
    os.mkdir('/'.join([USERS_FOLDER,new_user_folder]))
    os.mkdir('/'.join([USERS_FOLDER,new_user_folder,'audio']))
    os.mkdir('/'.join([USERS_FOLDER,new_user_folder,'video']))
    os.mkdir('/'.join([USERS_FOLDER,new_user_folder,'faces']))
    return USERS_FOLDER + '/' + new_user_folder



def listen(audio_file_name):
    '''Listens speech and records it.
    Args:
        audio_file_name: audio file name
    '''

    #create audio stream
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1,
                    rate=16000, input=True, frames_per_buffer=1024)
    stream.start_stream()
    buf = b''
    listen_start = time.time()
    #records audio
    while time.time() - listen_start < MSG_DURATION:
        chunk = stream.read(1024)
        buf += chunk

    #stop audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    #create and save recorded audio file
    waveFile = wave.open(audio_file_name, 'wb')
    waveFile.setnchannels(1)
    waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    waveFile.setframerate(16000)
    waveFile.writeframes(buf)
    waveFile.close()


def view():
    '''Views, records video and also saved faces if person is new.
    '''
    
    detector = FaceDetector()

    cap = cv2.VideoCapture(1)

    start = time.time()

    #"heat" webcam
    while time.time() - start <= 3:
        cap.read()

    face_captured = False
    
    #find person
    while not face_captured:
        ret, frame = cap.read()
        faces = detector.detect(frame)
        user_folder = None
        if len(faces) > 0:
            face_captured = True
            face = faces[0]
            face_poly = face.bounding_poly
            x = face_poly['x']
            y = face_poly['y']
            w = face_poly['w']
            h = face_poly['h']
            user_folder = find_person(frame[y:y+h,x:x+h])
    
    #set or create user`s folders    
    if not user_folder is None:
        write_faces = False
    else:
        write_faces = True
        user_folder = create_new_user_folder()
    print('user folder', user_folder)
    audio_record_folder = user_folder + '/' + 'audio'
    video_record_folder = user_folder + '/' + 'video'
    if write_faces:
        print('*')
        face_record_folder = user_folder + '/' + 'faces'
        counter = 0

    #get video and audio files name
    video_name = user_folder + '/video/' + str(len(os.listdir(video_record_folder)) + 1) + '.avi'
    audio_name = user_folder + '/audio/' + str(len(os.listdir(audio_record_folder)) + 1) + '.wav'
    #preparing for video record
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_name, fourcc, 8.0, (640,480))

    #create process for listening starting 
    audio_process = mpr.Process(target=listen, args=(audio_name,))
    start_msg = time.time()
    if write_faces:
        face_read_time = time.time()
    audio_process.start()

    #start write message
    while time.time() - start_msg < MSG_DURATION:
        
        ret, frame = cap.read()
        if ret:
            #add frane to video
            out.write(frame)
            #if person is new save person faces without duplicates
            if write_faces and (time.time() - face_read_time >= 1):
                faces = detector.detect(frame)
                if len(faces) > 0:
                    face = faces[0]
                    face_poly = face.bounding_poly
                    x = face_poly['x']
                    y = face_poly['y']
                    w = face_poly['w']
                    h = face_poly['h']
                    
                    face_img = frame[y:y+h, x:x+w]
                    exists = face_already_exists(face_img)
                    if not exists:
                        cv2.imwrite(face_record_folder + '/' + str(counter) + '.jpg', face_img)
                        all_saved_faces.append(face_img)
                        counter += 1
            

        time.sleep(0.01)

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def main():
    try:
        #create folder for users folders
        if not os.path.exists(USERS_FOLDER):
            os.mkdir(USERS_FOLDER)
        #create and start viewing process
        view_process = mpr.Process(target=view)
        view_process.start()
    except Exception as e:
        logging.error(str(e))
    
if __name__ == '__main__':
    main()
    
