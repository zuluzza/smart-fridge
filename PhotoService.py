from FridgeCamera import FridgeCamera
from datetime import datetime
from time import sleep
import time

class PhotoService:
    def __init__(self, *args, **kwargs):
        self.stop = False
        self._camera = FridgeCamera()

    def run(self):
        while not self.stop:
            #TODO replace with door open detection to start a video
            videoName = "video_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S"))
            self._camera.startVideo(videoName)
            sleep(10)
            self._camera.endVideo()
            
            self._camera.takePicture("picture_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S")))
        
    def stop(self):
        self.stop = True
        
#TODO for testing now, to be removed when usage is moved up to a higher lever
if __name__ == "__main__":
    photoService = PhotoService()
    photoService.run()
    exit(0)
