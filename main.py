import cv2 as cv
from time import sleep
from queue import Queue
from threading import Thread
from saveVideo import SaveVideo
from multitimer import MultiTimer


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

    def process_frame(self, video_length, preview=True,):
        sleep(3) # Wait for the first frames to come in
        timer = MultiTimer(video_length, self.recorder.save_stream, runonstart=False)
        timer.start()

        while True:
            frame = self.frame_queue.get()

            if self.recorder.isOpened():
                self.recorder.write_frame(frame)

            if preview:
                cv.imshow("Camera", frame)
            
            if cv.waitKey(1) & 0xFF == ord('q'):
                self.recorder.save_stream(perm=True)
                break
        


if __name__ == "__main__":
    prog = Program()
    stream_thread = Thread(target=prog.get_stream, args=())
    process_thread = Thread(target=prog.process_frame, args=((10,)), kwargs={'preview':True})
    stream_thread.start()
    process_thread.start()


# def main_loop():

#     while True:
#         ret, frame = vcap.read()
#         # show image if it could be retrieved from stream
#         if ret:
#             cv.imshow("video", frame)

#             if recorder is not None and recorder.isOpened():
#                 recorder.write_frame(frame)

#         if cv.waitKey(1) & 0xFF == ord('q'):
#             break
            

#     vcap.release()
#     recorder.close_stream(full_stop=True)
#     cv.destroyAllWindows()





# vcap = cv.VideoCapture("udp://192.168.0.32:5000/")
# recorder = None

# if vcap.isOpened():
#     main_loop()

