import Rpi as rpi

rpi.init()	# Rpi initialization routine
psm = rpi.psm	# Get PiStorms

# With just P:
#	pGain = 0.43
#	basePower = 35
#	offset = 500

basePower = 35 # Base speed regardless of turning
offset = 500 # Offset for the middle of light sensor data
pGain = 0.32 # Proportional intensity
iGain = 0.1 # Integral intensity
iMax = 1000; # Integral max value
iMin = -1000; # Integral min value

totalError = 0 # Integral of error should start at 0 to have no affect 

while (not psm.isKeyPressed()):
	lightSens = psm.BBS1.lightSensorNXT()

	####	PI Controller
	error = lightSens - offset # How far off the robot is from the offset
	totalError += error # iterate the integral of error
	totalError = (totalError > iMax) ? iMax : (totalError < iMin) ? iMin : totalError # Limit integral on the range [iMin,iMax]
	totalError = (-15 <= error and error <= 15) ? 0 : totalError # Reset integral term on the error range [iResetMin,iResetMax]
	output = pGain * error + iGain * totalError # Combine Proportion and Integral terms

	psm.BBM2.setSpeed(-1 * (-1 * output + basePower))
	psm.BBM1.setSpeed(-1 * (output + basePower))

rpi.dinit() # Rpi deinitialize routine
