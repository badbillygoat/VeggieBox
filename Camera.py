#import necessary librares
import datetime
from time import sleep
from picamera import PiCamera

#define function that will be called to activate camera:
def camera(picinterval,numberofpics):
    now = datetime.datetime.now()
    camera = PiCamera()
    camera.rotation = 180
    camera.resolution = (1024, 768)
    camera.start_preview()
    camera.annotate_text = str(now)
    # Camera warm-up time
    for i in range(numberofpics):
        sleep(picinterval)
        camera.capture('/home/pi/Documents/Programming/Camera Tests/TestPics/image%s.jpg' % i)
    camera.stop_preview()
