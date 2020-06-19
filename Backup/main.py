from saveVideo import SaveVideo
import cv2 as cv
import multitimer 
from time import sleep




def start_recorder(recorder):
    recorder = SaveVideo()
    return recorder

def main_loop():
    while True:
        ret, frame = vcap.read()
        if ret:
            cv.imshow("video", frame)

            if recorder is not None:
                recorder.write_frame(frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            break
            

    vcap.release()
    timer.stop()
    recorder.close_stream(full_stop=True)
    cv.destroyAllWindows()





vcap = cv.VideoCapture("udp://192.168.0.32:5000/")
recorder = None
# How often the stream should be saved to harddrive (mins)
time_interval = 20
timer = multitimer.RepeatingTimer(time_interval, recorder.close_stream, count=-1, runonstart=False) # timer that repeats every interval
timer_rec = multitimer.MultiTimer(8, start_recorder, kwargs=dict(recorder), runonstart=False)

if vcap.isOpened():
    timer.start()
    timer_rec.start()
    main_loop()

