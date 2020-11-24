# smart-fridge

A fridge camera when you are grocery shopping but cannot recall what you have already in your fridge! 

Utilizes raspberry pi with camera module to take a short video of your fridges contents and sends it to your dropbox to be viewed from anywhere. Video capture is initiated when you open the door of fridge by detecting if door is open with a light sensor.

There is also an android app to view the video that you can find in https://github.com/zuluzza/smart-fridge-app

## Requirements and installation
Requires python3, raspberry pi with working camera module and connected light sensor. 

How to connect and enable camera module can be found in https://projects.raspberrypi.org/en/projects/getting-started-with-picamera

The light sensor used in the project is https://www.partco.fi/fi/elektroniikan-komponentit/anturit/valo/19099-spf-bob-08688.html Connect it to raspberry pi's GPIO27, ground and 3.3V.

pip install dropbox

sudo apt install gpac

Create a dropbox token in https://www.dropbox.com/developers/apps/create
Place the created token it to "dropbox_token.txt" text file in project root directory.

## Running

python PhotoService.py
