import cv2
import time


class PhotoCapture:
    ''' Allows to capture frame from web-camera and to save it as image'''

    def __init__(self, init_time=2):
        '''Constructor
    Args:
        init_time: time for initialize camera, needs to make bright photo
        '''
        
        self.camera = cv2.VideoCapture(0)
        self.init_time = init_time
        
    def make_photo(self, save_path=None):
        '''Makes photo and saves it on disk
        Args:
            save_path: path to save photo
        Returns:
            save_path: path to save photo
        '''
        
        start_time = time.time()
        if save_path is None:
            save_path = 'image.jpg'
        while True:
            ret, frame = self.camera.read()
            cv2.imwrite(save_path, frame)
                
            if time.time() - start_time >= self.init_time:
                break
            
        return save_path

    def __del__(self):
        '''Destructor'''
        self.camera.release()

        
        
class VideoRecorder:
    '''Allows to record video from camera to file'''

    def __init__(self, fps=8.0, width=640, height=480, fourcc='XVID'):
        '''Constructor
        Args:
            fps: frame frequency per second; normal frequency value
                 depends on camera type; you can take as normal frequency
                 average of your camera FPS
            width: video frame width
            height: video frame height
            fourcc: video codec type; details: http://www.fourcc.org/codecs.php
        '''
        
        self.camera = cv2.VideoCapture(0)
        self.fps = fps
        self.width = width
        self.height = height
        self.fourcc = cv2.VideoWriter_fourcc(*fourcc)

    def record_video(self, save_path=None, duration=5):
        '''Records and saves video
        Args:
            save_path: path to save video
            record_time: video duration in seconds
        Returns:
            save_path: path to save video
        '''

        if save_path is None:
            save_path = 'video.avi'
            
        out = cv2.VideoWriter(save_path,self.fourcc, self.fps,
                              (self.width,self.height))
        start_time = time.time()
        while time.time() - start_time <= duration:
            ret, frame = self.camera.read()
            if ret == True:
                out.write(frame)

        return save_path
    

    def __del__(self):
        '''Destructor'''
        
        self.camera.release()
            
