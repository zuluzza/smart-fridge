from FridgeCamera import FridgeCamera
from datetime import datetime
from time import sleep
import time

class DropboxCloud:
    def __init__(self, access_token):
        self._accessToken = access_token

    def uploadFile(filename):
        dbx = dropbox.Dropbox(self._accessToken)

        with open(filename, "rb") as file:
            # this is for uploading < 150MB files. Let's trust it's enough
            dbx.files_upload(file, "smart_fridge/" + filename)

class PhotoService:
    def __init__(self):
        self.stop = False
        self._camera = FridgeCamera()
        self._dropboxCloud = None

    def initDropboxCloud(self):
        # The file is expected to contain the token only on first line. This whole token handling could be improved
        with open("dropbox_token.txt", "r") as file:
            token = file.readline()
            self._dropboxCloud = DropboxCloud(token.strip())

    def run(self):
        while not self.stop:
            #TODO replace with door open detection to start a video
            videoName = "video_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S"))
            self._camera.startVideo(videoName)
            sleep(10)
            self._camera.endVideo()
            if self._dropboxCloud != None:
                self._dropboxCloud.uploadFile(filename)
            #self._camera.takePicture("picture_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S")))
        
    def stop(self):
        self.stop = True

#TODO for testing now, to be removed when usage is moved up to a higher lever
if __name__ == "__main__":
    photoService = PhotoService()
    photoService.run()
    exit(0)
