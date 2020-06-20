from time import sleep
from queue import Queue
from threading import Thread

import cv2 as cv

from multitimer import MultiTimer

from savevideo import SaveVideo
from motiondetect import MotionDetection


class Program:

    def __init__(self):
        self.cap = cv.VideoCapture("udp://192.168.0.32:5000/")
        self.frame_queue = Queue()
        self.recorder = SaveVideo()

    def get_stream(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                self.frame_queue.put(frame)

    def process_frame(self, video_length, preview=True):
        sleep(3) # Wait for the first frames to come in

        md = MotionDetection()

        timer = MultiTimer(video_length, self.recorder.save_stream, runonstart=False)
        timer.start()

        while True:
            frame = self.frame_queue.get()

            # md.process_frame(frame)

            if self.recorder.is_open():
                self.recorder.write_frame(frame)

            if preview:
                cv.imshow("Camera", frame)
 
            if cv.waitKey(1) & 0xFF == ord('q'):
                self.recorder.save_stream(perm=True)
                break

    # def motion_detection(self):
    #     while True:

    #     pass


if __name__ == "__main__":
    prog = Program()
    stream_thread = Thread(target=prog.get_stream, args=())
    process_thread = Thread(target=prog.process_frame, args=((10,)), kwargs={'preview':True})
    stream_thread.start()
    process_thread.start()
