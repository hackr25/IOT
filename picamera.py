To capture image:
import picamera
from time
import sleep
#create object for PiCamera class

#set resolution
camera.resolution = (1024, 768)

camera.start_preview()
#add text on image
camera.annotate_text = 'Hi Pi User'
sleep(5)
#store image

camera.stop_preview()
To capture video:
import picamera
from time import sleep


print()
#start recording using pi camera

#wait for video to record

#stop recording


print("video recording stopped")
To Play the video:
Omxplayer demo.h264