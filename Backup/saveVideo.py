import os
import cv2 as cv
import datetime
import random



class SaveVideo:
    FOURCC = cv.VideoWriter_fourcc(*'XVID')         # Format
    FPS = 30                                        # FPS of the stream         
    DIMS = (1280, 720)                              # Resolution of the stream

    def __init__(self):
        self.make_folder()                          # Make recordings folder                                                                                  
        self.filename = self.get_filename()         # Directory and filename     
        self.outstream = self.get_outstream()

    def write_frame(self, frame):
        self.outstream.write(frame)

    def close_stream(self, full_stop=False):
        self.outstream.release()
        self.outstream = None
        self.filename = self.get_filename()
        if not full_stop:
            self.outstream = self.get_outstream()

    def get_outstream(self):
        return cv.VideoWriter(self.filename, self.FOURCC, self.FPS, self.DIMS)

    def get_filename(self) -> str:
        filename = "Recordings/" + datetime.datetime.now().strftime("%Y-%m-%d %H-%M" + ".avi")
        if os.path.isfile(filename):
            index = filename.find('.')
            return filename[:index] + " (" + str(random.randint(1,20)) + ")" + filename[index:]
        return filename

    def isOpen(self) -> bool:
        return self.outstream.isOpened()

    def make_folder(self):
        if not os.path.exists(os.path.dirname(os.path.realpath(__file__)) +  "\Recordings"):
            os.makedirs(os.path.dirname(os.path.realpath(__file__)) +  "\Recordings", exist_ok=False)

if __name__ == '__main__':
    sv = SaveVideo()

    