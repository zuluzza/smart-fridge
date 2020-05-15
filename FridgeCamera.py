from piCamera import PiCamera
from time import sleep
from datetime import datetime

class FridgeCamera():

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._camera = PiCamera();
        self._capturingVideo = False

    def takePicture(filename):
        if (self._capturingVideo):
            return
        self._camera.resolution = (2592, 1944)
        self._camera.start_preview()
        # at least 2 secs sleeps is required for camera to sense light levels
        sleep(2)
        self._camera.annotate_text = datetime.now
        self._camera.capture(filename)
        self._camera.stop_preview()

    def startVideo(filename):
        if (self._capturingVideo):
            return
        self._capturingVideo = True
        self._camera.resolution = (1920, 1080)
        self._camera.start_preview()
        self._camera.annotate_text = datetime.now
        self._camera.startRecording(filename)

    def endVideo():
        if (self._capturingVideo):
            self._capturingVideo = False
            self._camera.stop_recording()
            self._camera.stop_preview()
