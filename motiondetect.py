import cv2 as cv
import numpy as np



class MotionDetection:
    def __init__(self):
        self.fbgb = cv.createBackgroundSubtractorMOG2(300, 400, True)
        self.framecount = 0

    def process_frame(self, frame):
        self.framecount += 1

        # Resize the image
        resized_frame = cv.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Get the foreground mask
        fgmask = self.fbgb.apply(resized_frame)

        # Count all the non zero pixels within the mask
        count = np.count_nonzero(fgmask)

        if self.framecount > 1 and count > 5000:
            print("Movement")
        
        cv.imshow("Resized Frame", resized_frame)
        cv.imshow("Mask", fgmask)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cv.destroyAllWindows()



