import cv2 as cv
import numpy as np



class MotionDetection:
    def __init__(self):
        # Tries to find background by looking at history of frames
        self.bgs = cv.createBackgroundSubtractorMOG2(300, 400, True)
        self.framecount = 0

    def process_frame(self, frame):
        self.framecount += 1

        # Resize the image for faster processing
        resized_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Get the foreground mask
        fgmask = self.bgs.apply(resized_frame)

        # Count all the non zero pixels within the mask
        count = np.count_nonzero(fgmask)

        # Decides when a detection is to be triggered
        if self.framecount > 1 and count > 5000:
            print("Movement")
        
        cv.imshow("Resized Frame", resized_frame)
        cv.imshow("Mask", fgmask)

        # Close window when 'q' is pressed
        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()



