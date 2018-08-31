# a test to see if we can integrate OpenCV video recording with Flask
# comes from https://github.com/log0/video_streaming_with_flask_example
import cv2
import threading

class RecordingThread (threading.Thread):
    def __init__(self, name, camera):
        threading.Thread.__init__(self)
        self.name = name
        self.isRunning = True
 
        self.cap = camera
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        self.out = cv2.VideoWriter('./static/video.mp4',fourcc, 20.0, (640,480))
 
    def run(self):
        while self.isRunning:
            ret, frame = self.cap.read()
            if ret:
                self.out.write(frame)
 
        self.out.release()
 
    def stop(self):
        self.isRunning = False
 
    def __del__(self):
        self.out.release()

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        # self.video = cv2.VideoCapture(0)
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        self.video = cv2.VideoCapture('video.mp4')
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()