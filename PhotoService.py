import FridgeCamera
from datetime import datetime
from time import sleep

class PhotoService(self):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._camera = FridgeCamera()

    def run(self):
        while not self.stop:
            #TODO replace with door open detection to start a video
            self._camera.startVideo("video_{}".format(datetime.now().strftime(strftime("%m/%d/%Y_%H:%M:%S"))))
            sleep(10)
            self.camera.stopVideo()

    def stop(self):
        self.stop = True

#TODO for testing now, to be removed when usage is moved up to a higher lever
if __name__ == "__main__":
    photoService = PhotoService()
    photoService.run
    exit(0)