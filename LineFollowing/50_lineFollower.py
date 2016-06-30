import Rpi as rpi

debugOnly = True

rpi.init()

# Rudimentary line follower
while (not psm.isKeyPressed()):
	leftSens = psm.BBS1.lightSensorNXT()
	rightSens = psm.BBS2.reflectedLightSensorEV3()
	psm.screen.termPrintln(str(leftSens )+ "   :::   " + str(rightSens))

	if (not debugOnly)
		psm.BBM1.setSpeed(50)
		psm.BBM1.setSpeed

rpi.dinit()