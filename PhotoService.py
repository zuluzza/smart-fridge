from FridgeCamera import FridgeCamera
from datetime import datetime
from time import sleep
import time
import dropbox
import os

class DropboxCloud:
    def __init__(self, access_token):
        self._accessToken = access_token

    def uploadFile(self, filename):
        dbx = dropbox.Dropbox(self._accessToken)

        with open(filename, "rb") as f:
            # this is for uploading < 150MB files. Let's trust it's enough
            #Note dropbox requires filename starts with '/'
            dbx.files_upload(f.read(), "/video_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S")))

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

    def stop(self):
        self.stop = True

    def run(self):
        i = 0
        while not self.stop:
            #TODO replace with door open detection to start a video
            videoName = "video_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S"))
            print("starting video")
            videoName = self._camera.startVideo(videoName)
            sleep(5)
            print("stopping video")
            self._camera.endVideo()
            if self._dropboxCloud != None:
                print("uploading to dropbox")
                self._dropboxCloud.uploadFile(videoName)
                #remove file when done uploading
                os.remove(videoName)
            #self._camera.takePicture("picture_{}".format(datetime.now().strftime("%m.%d.%Y_%H:%M:%S")))

            i += 1
            if (i > 4):
                self.stop = True

#TODO for testing now, to be removed when usage is moved up to a higher lever
if __name__ == "__main__":
    photoService = PhotoService()
    photoService.initDropboxCloud()
    photoService.run()
    exit(0)
