from FridgeCamera import FridgeCamera
from DoorState import DoorState
from datetime import datetime
from time import sleep
import time
import dropbox
import os

DATE_FORMAT_STRING = "%m_%d_%Y_%H_%M_%S"
class DropboxCloud:
    def __init__(self, access_token):
        self._accessToken = access_token

    def uploadFile(self, filename):
        dbx = dropbox.Dropbox(self._accessToken)

        with open(filename, "rb") as f:
            # this is for uploading < 150MB files. Let's trust it's enough
            #Note dropbox requires filename starts with '/'
            dbx.files_upload(f.read(), "/video_{}".format(datetime.now().strftime(DATE_FORMAT_STRING)))

class PhotoService:
    def __init__(self):
        self.stop = False
        self._camera = FridgeCamera()
        self._door = DoorState()
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
        capturingVideo = False #replace with a attribute of the camera?
        while not self.stop:
            print("running with door state {} and capturing {}".format(self._door.getState(), capturingVideo))
            if self._door.getState() and not capturingVideo:
                videoName = "video_{}".format(datetime.now().strftime(DATE_FORMAT_STRING))
                print("starting video")
                self._camera.startVideo(videoName)
                capturingVideo = True
                sleep(5) #forces minimum length for video
            if capturingVideo and not self._door.getState():
                print("stopping video")
                self._camera.endVideo()
                capturingVideo = False
                if self._dropboxCloud != None:
                    videoName = videoName + ".mp4"
                    print("uploading to dropbox {}".format(videoName))
                    self._dropboxCloud.uploadFile(videoName)
                    #remove file when done uploading
                    os.remove(videoName)
                    
                i += 1
                if (i > 4):
                    self.stop = True
            sleep(1)
            #self._camera.takePicture("picture_{}".format(datetime.now().strftime(DATE_FORMAT_STRING)))

#TODO for testing now, to be removed when usage is moved up to a higher lever
if __name__ == "__main__":
    photoService = PhotoService()
    photoService.initDropboxCloud()
    photoService.run()
    exit(0)
