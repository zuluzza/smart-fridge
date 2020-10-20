from picamera import PiCamera
from time import sleep
from datetime import datetime
import os
from subprocess import call

class FridgeCamera():

    def __init__(self, *args, **kwargs):
        self._camera = PiCamera();
        self._capturingVideo = False
        self._filenameNoFormat = ""

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
        filename = "/home/pi/smart-fridge/" + filename
        self._filenameNoFormat = filename
        filename = filename + ".h264"
        self._camera.resolution = (1920, 1080)
        self._camera.annotate_text = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        self._camera.start_recording(filename)
        return filename

    def convert(self, filename_h264, filename_mp4):
        command = "MP4Box -add " + filename_h264 + " " + filename_mp4
        call([command], shell=True) 
        
    def endVideo(self):
        if (self._capturingVideo):
            self._capturingVideo = False
            self._camera.stop_recording()
            self._camera.stop_preview()
            self.convert(self._filenameNoFormat + ".h264", self._filenameNoFormat + ".mp4")
            return self._filenameNoFormat + ".mp4"
        return ""
