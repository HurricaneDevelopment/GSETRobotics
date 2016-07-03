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
dGain = 0.3 # Derivative intensity
iMax = 1000; # Integral max value
iMin = -1000; # Integral min value
prevError = 0;

totalError = 0 # Integral of error should start at 0 to have no affect 

while (not psm.isKeyPressed()):
	lightSens = psm.BBS1.lightSensorNXT()

	####	PI Controller
	error = lightSens - offset # How far off the robot is from the offset
	totalError += error # iterate the integral of error
	totalError = iMax if totalError > iMax else iMin if totalError < iMin else totalError # Limit integral on the range [iMin,iMax]
	totalError = 0 if -15 <= error and error <= 15 else totalError # Reset integral term on the error range [iResetMin,iResetMax]
	dState = error - prevError
	output = pGain * error + iGain * totalError + dGain * dState # Combine Proportion and Integral terms

	psm.BBM2.setSpeed(-1 * (-1 * output + basePower)) # Left motor power
	psm.BBM1.setSpeed(-1 * (output + basePower)) # Right motor power

rpi.dinit() # Rpi deinitialize routine 
