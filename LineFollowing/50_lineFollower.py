import Rpi as rpi

def isDark( val ):
	return val >= 50 and val <= 70
def isLight( val ):
	return val >= 35 and val <= 50

debugOnly = True

rpi.init()
psm = rpi.psm

prevLeftLight = True
#prevRightLight = False

pGain = 0.43 # How intense the turning will be
basePower = 35 # Base speed regardless of turning
offset = 500 # offset for the middle of light sensor data

# Rudimentary line follower
while (not psm.isKeyPressed()):
	leftSens = psm.BBS1.lightSensorNXT()
#	rightSens = psm.BBS2.reflectedLightSensorEV3()
	#psm.screen.termPrintln(str(leftSens )+ "   :::   " + str(rightSens))
#	psm.screen.termPrint(str(leftSens))
#	psm.screen.termPrint(" ::: ")

	error = leftSens - offset
#	psm.screen.termPrintln(str(error))
	psm.BBM2.setSpeed(-1 * (-1 * error * pGain + basePower))
	psm.BBM1.setSpeed(-1 * (error * pGain + basePower))
'''
	if (not debugOnly):
		if prevLeftLight == isLight( leftSens ) and isLight( leftSens ) and prevRightLight == isLight( rightSens ) and isDark( rightSens ):
			#Keep going straight, maybe increase speed
			psm.BBM1.setSpeedSync(50)
		elif  prevLeftLight == isLight( leftSens ) and isLight( leftSens ) and  not prevRightLight and isLight( rightSens ):
			#Was straight, now is left of the path
			psm.BBM1.setSpeed(50)
			psm.BBM2.setSpeed(25)
		elif  prevLeftLight  and isDark( leftSens ):
			#Was straight, now is right of the path
			psm.BBM1.setSpeed(25)
			psm.BBM1.setSpeed(50)
'''
		#prevLeftLight = isLight( leftSens )
		#prevRightLight = isLight( rightSens )
rpi.dinit()
