import Rpi as rpi
from PID import PID

rpi.init()	# Rpi initialization routine
psm = rpi.psm	# Get PiStorms

basePower = 35 # Base speed regardless of turning
offset = 500 # Offset for the middle of light sensor data
kP = 0.13 # Proportional intensity
kI = 0.0 # Integral intensity
kD = 0.0 # Derivative intensity
iMin = -1000; # Integral min value
iMax = 1000; # Integral max value

lightSens = psm.BBS1.lightSensorNXT()

pid = PID(offset,kP,kI,kD,iMin,iMax,lightSens,-1 * basePower,basePower)

while (not psm.isKeyPressed()):
	lightSens = psm.BBS1.lightSensorNXT()

	output = pid.calculate(lightSens) # Get PID output
	psm.BBM2.setSpeed(-1 * (-1 * output + basePower)) # Left motor power
	psm.BBM1.setSpeed(-1 * (output + basePower)) # Right motor power

rpi.dinit() # Rpi deinitialize routine 
