from picamera import PiCamera
from time import sleep
from datetime import datetime
import os

class FridgeCamera():

    def __init__(self, *args, **kwargs):
        self._camera = PiCamera();
        self._capturingVideo = False

    def takePicture(self, filename):
        if (self._capturingVideo):
            return
        with self._camera as camera:
            camera.resolution = (2592, 1944)
            camera.start_preview()
            # at least 2 secs sleeps is required for camera to sense light levels
            sleep(2)
            camera.annotate_text = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            camera.capture(filename)
            camera.stop_preview()

    def startVideo(self, filename):
        if (self._capturingVideo):
            return
        self._capturingVideo = True
        filename = "/home/pi/smart-fridge/" + filename + ".h264"
        with self._camera as camera:
            camera.resolution = (1920, 1080)
            camera.annotate_text = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
            camera.start_recording(filename)

    def endVideo(self):
        if (self._capturingVideo):
            self._capturingVideo = False
            self._camera.stop_recording()
            self._camera.stop_preview()
