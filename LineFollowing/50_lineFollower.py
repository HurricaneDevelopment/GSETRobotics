import Rpi as rpi

rpi.init()
psm = rpi.psm

basePower = 35 # Base speed regardless of turning
offset = 500 # Offset for the middle of light sensor data
pGain = 0.43 # Proportional intensity
iGain = 0.2
iMax = 0;
iMin = 0;

totalError = 0

# Rudimentary line follower
while (not psm.isKeyPressed()):
	lightSens = psm.BBS1.lightSensorNXT()

	#PI Controller
	error = lightSens - offset
	totalError += error
	totalError = (totalError > iMax) ? iMax : (totalError < iMin) ? iMin : totalError
	output = pGain * error + iGain * totalError

	psm.BBM2.setSpeed(-1 * (-1 * output+ basePower))
	psm.BBM1.setSpeed(-1 * (output + basePower))

rpi.dinit()