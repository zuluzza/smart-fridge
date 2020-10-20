from gpiozero import LightSensor

class DoorState():

    def __init__(self, *args, **kwargs):
        # hard coded Light Sensor to be wired to GPIO27
        time_constant = 1.6*10**-1
        self._ldr = LightSensor(27, charge_time_limit=time_constant)
        self._isOpen = self._ldr.light_detected
        self._ldr.when_dark = self.onDark
        self._ldr.when_light = self.onLight
        print("LDR initialized with charge_time_limit={}".format(time_constant))

    def getState(self):
        return self._isOpen

    def onLight(self):
        print("light detected")
        self._isOpen = True
        
    def onDark(self):
        print("darkness upon us")
        self._isOpen = False
    
    def waitUntilOpened(self):
        self._ldr.wait_for_light()

    def waitUntilClosed(self):
        self._ldr.wait_for_dark()



