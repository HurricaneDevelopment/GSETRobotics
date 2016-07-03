import Rpi as rpi
from PID import PID
from threading import Thread

rpi.init()      # Rpi initialization routine
psm = rpi.psm   # Get PiStorms

basePower = 22 # Base speed regardless of turning
offset = 500 # Offset for the middle of light sensor data
kP = 0.7 # Proportional intensity
kI = 0.04 # Integral intensity
kD = 3.7 # Derivative intensity
iMin = -1500; # Integral min value
iMax = 1500; # Integral max value
overUnder = 30
resetZone = 30

def readnewGains():
        while (not psm.isKeyPressed()): 
                gainsString = raw_input("Type Gains:")
                gainsArray = gainsString.split(",") 
                pid.setGains(float(gainsArray[0]),float(gainsArray[1]),float(gainsArray[2]));
		basePower = int(gainsArray[3]);

lightSens = psm.BBS1.lightSensorNXT()

pid = PID(offset,kP,kI,kD,iMin,iMax,lightSens,-1 * basePower - overUnder,basePower + overUnder,-1 * resetZone,resetZone)

gg = Thread(target=readnewGains)
gg.start()

while (not psm.isKeyPressed()):
        lightSens = psm.BBS1.lightSensorNXT()

        output = pid.calculate(lightSens) # Get PID output
        psm.BBM2.setSpeed(-1 * (-1 * output + basePower)) # Left motor power
        psm.BBM1.setSpeed(-1 * (output + basePower)) # Right motor power

rpi.dinit() # Rpi deinitialize routine
