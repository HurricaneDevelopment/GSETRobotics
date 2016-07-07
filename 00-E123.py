import Rpi as rpi
from HiTechnicColorV2 import HiTechnicColorV2
from PID import PID
from threading import Thread
from time import sleep
import sys

### ===/// HELP \\\=== ###
#	BAM1: Ball Cage and Ultrasonic
#	BAM2:   BROKEN DO NO USE
#	BBM1: Right Drive
#	BBM2: Left Drive
#	BAS1: Light Sensor
#	BAS2: Ultrasonic
#	BBS1:   UNUSED
#	BBS2: Color Sensor
### ===/// END HELP \\\=== ###

### ===/// CONFIGURATION \\\=== ###
basePower = 20 # Base speed regardless of turning 							# PID
offset = 500 # Offset for the middle of light sensor data
kP = 1 # Proportional intensity
kI = 0 # Integral intensity
kD = 0 # Derivative intensity
iMin = -1500; # Integral min value
iMax = 1500; # Integral max value
overUnder = 30 # Maximum PID output
resetZone = 30 # Range to reset integral
ballUltrasonicError = 4 # Differnce in expected ultrasonic input in cm		# Find the ball
obstacleAvoidZone = 5 # How close to get to the obstacle before running evasive maneuvers
moveSleepTime = 100 # How long to wait at the end of every move.  Measured in milliseconds
### ===/// END CONFIGURATION \\\=== ###

### ===/// PROCCESS VARIABLES \\\=== ###
previousColor = -999
victims = 0
ballLocation = 0
ballLocated = False
obstacleEncountered = False
# Threading
exitMain = False
countVictimsStatus = False
exitCountVictims = False
### ===/// END PROCCESS VARIABLES \\\=== ###

rpi.init()      # Rpi initialization routine
psm = rpi.psm   # Get PiStorms

#Initialize I2C Hitechnic Color
hc=HiTechnicColorV2()
psm.BBS2.activateCustomSensorI2C()

# Count the victims in a seperate thread asynchronously
def countVictims():
	countVictimsStatus = True
	
	while countVictimsThreadStatus && not exitCountVictims && not exitMain:
		color = hc.get_colornum()
		if color != previousColor:
			previousColor = color
			if previousColor == 2 or previousColor == 3:
				victims += 1
				sleep(3)
			elif previousColor == 8 or previousColor == 9:
				exitCountVictims = True
				exitMain = True
		sleep(0.2)

	countVictimsStatus = False

def driveForward(degrees,power=100):
	psm.BBM1.runDegs(-1 * degrees,power,True,False)
	psm.BBM2.runDegs(-1 * degrees,power,True,False)
	while psm.BBM1.isBusy() or psm.BBM2.isBusy()
		sleep(moveSleepTime / 1000.0)

def driveReverse(degrees,power=100):
	driveForward(-1 * degrees,power)

def pivotRight(degrees,power=100):
	psm.BBM1.runDegs(degrees,power,True,False)
	psm.BBM2.runDegs(-1 * degrees,power,True,False)
	while psm.BBM1.isBusy() or psm.BBM2.isBusy()
		sleep(moveSleepTime / 1000.0)

def pivotLeft(degrees,power=100):
	pivotRight(-1 * degrees,power)

def turnRight(degrees,power=100):
	psm.BBM2.runDegs(-1 * degrees,power,True,False)
	while psm.BBM2.isBusy()
		sleep(moveSleepTime / 1000.0)

def turnLeft(degrees,power=100):
	psm.BBM1.runDegs(-1 * degrees,power,True,False)
	while psm.BBM1.isBusy()
		sleep(moveSleepTime / 1000.0)

def foundBall():
	for i in range(0,5):
		psm.led(1,255,5,5)
		psm.led(2,5,255,5)
		sleep(0.33)
		psm.led(2,255,5,5)
		psm.led(1,5,255,5)
		sleep(0.33)
	psm.led(1,5,255,5)
	psm.led(2,5,255,5)
	ballLocated = True

def grabBall():
	# function to grab the ball

### ===/// SECTION: Line Follower \\\=== ###
lightSens = psm.BAS1.lightSensorNXT()
pid = PID(offset,kP,kI,kD,iMin,iMax,lightSens,-1 * basePower - overUnder,basePower + overUnder,-1 * resetZone,resetZone)

cV = Thread(target=countVictims)
cV.start()

while (not exitMain):
        lightSens = psm.BAS1.lightSensorNXT()
        output = pid.calculate(lightSens) # Get PID output
        psm.BBM2.setSpeed(-1 * (-1 * output + basePower)) # Left motor power
        psm.BBM1.setSpeed(-1 * (output + basePower)) # Right motor power
        if psm.isKeyPressed():
        	rpi.dinit()
        	sys.exit("Aborted")
        if not obstacleEncountered and psm.BAS2.ultrasonic() <= obstacleAvoidZone:
        	obstacleEncountered = True
        	pivotLeft(360)
        	driveForward(360)
        	pivotRight(360)
        	driveForward(460)
        	pivotRight(360)
        	driveForward(325)
        	pivotLeft(360)
exitMain = False

###
###
### DO SOMETHING TO UNLOCK ULTRASONIC SENSOR
###
###

### ===/// SECTION: Locate Ball \\\=== ###
while not ballLocated:
	if ballLocation == 0: # Shearching for ball in location 0
		expectedDistance = 25
		driveForward(100)
		pivotLeft(360)
		driveForward(800)
		if abs(psm.BAS2.ultrasonic() - expectedDistance) >= ballUltrasonicError:
			foundBall()
		else:
			ballLocation += 1
	elif ballLocation == 1: # Shearching for ball in location 1
		expectedDistance = 25
		driveForward(150)
		if abs(psm.BAS2.ultrasonic() - expectedDistance) >= ballUltrasonicError:
			foundBall()
		else:
			ballLocation += 1
	elif ballLocation == 2: # Shearching for ball in location 2
		expectedDistance = 25
		driveReverse(550)
		pivotRight(360)
		driveForward(300)
		if abs(psm.BAS2.ultrasonic() - expectedDistance) >= ballUltrasonicError:
			foundBall()
		else:
			ballLocation += 1
	elif ballLocation == 3: # Shearching for ball in location 3
		expectedDistance = 25
		driveForward(300)
		if abs(psm.BAS2.ultrasonic() - expectedDistance) >= ballUltrasonicError:
			foundBall()
		else:
			ballLocation += 1
	elif ballLocation == 4: # Shearching for ball in location 4
			expectedDistance = 25
		driveReverse(600)
		pivotLeft(360)
		driveReverse(720)
		if abs(psm.BAS2.ultrasonic() - expectedDistance) >= ballUltrasonicError:
			foundBall()
		else:
			ballLocation += 1
	elif ballLocation == 5: # Shearching for ball in location 5
		expectedDistance = 25
		pivotRight(150)
		if abs(psm.BAS2.ultrasonic() - expectedDistance) >= ballUltrasonicError:
			foundBall()
		else:
			ballLocation += 1
	else: # No ball has been found
		rpi.dinit() # Rpi deinitialize routine
		sys.exit("The ball was not found")

### ===/// SECTION: Take The Ball \\\=== ###
if ballLocation == 0: # Retrieving ball from location 0
	driveForward(75)
	pivotLeft(360)
	driveReverse(500)
	grabBall()
	driveForward(500)
	turnLeft(360)
	driveForward(700)
	turnRight(360)
	driveForward(200)
elif ballLocation == 1: # Retrieving ball from location 1
	driveReverse(75)
	pivotLeft(360)
	driveReverse(500)
	grabBall()
	driveForward(500)
	turnLeft(360)
	driveForward(700)
	turnRight(360)
	driveForward(200)
elif ballLocation == 2: # Retrieving ball from location 2
	driveForward(50)
	pivotLeft(360)
	driveReverse(500)
	grabBall()
	driveForward(450)
	turnLeft(360)
	driveForward(75)
	turnLeft(360)
	driveForward(400)
	turnRight(360)
	driveForward(200)
elif ballLocation == 3: # Retrieving ball from location 3
	driveForward(400)
	pivotLeft(360)
	driveReverse(500)
	grabBall()
	driveForward(450)
	turnLeft(360)
	driveForward(750)
	turnLeft(360)
	driveForward(400)
	turnRight(360)
	driveForward(200)
elif ballLocation == 4: # Retrieving ball from location 4
	driveReverse(75)
	pivotLeft(360)
	driveReverse(500)
	grabBall()
	driveForward(500)
	turnRight(360)
	driveForward(400)
	turnLeft(360)
	driveForward(200)
elif ballLocation == 5: # Retrieving ball from location 5
	pivotLeft(150)
	pivotLeft(360)
	driveReverse(500)
	grabBall()
	driveForward(500)
	turnRight(360)
	driveForward(450)
	turnLeft(360)
	driveForward(200)
else: # No ball location was given
	rpi.dinit() # Rpi deinitialize routine
	sys.exit("There was not a vaild location for the ball")

rpi.dinit() # Rpi deinitialize routine