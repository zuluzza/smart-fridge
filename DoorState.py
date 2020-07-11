from gpiozero import LightSensor

class DoorState():
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # hard coded Light Sensor to be wired to GPIO27
        self._ldr = LightSensor(27)
        self._isOpen = self._ldr.light_detected

    def getState(self):
        return self._isOpen

    def waitUntilOpened(self):
        self._ldr.wait_for_light()

    def waitUntilClosed(self):
        self._ldr.wait_for_dark()



