from PiStorms import PiStorms
import time
import datetime

psm = PiStorms()
'''debugString = ""

def writeDebug( message ):
	global debugString
	debugString += str(message) + "\n"

def dinit():
	global debugString
	target = open("/var/robolog/" + datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S"),'w+')
	target.write(debugString)
	target.close()

	psm.BBM1.brakeSync()
	psm.BBM2.brakeSync()
'''
#writeDebug("===Starting Program===")
psm.BBM1.setSpeedSync(50)

while(not psm.isKeyPressed()):
	level = psm.BAS1.lightSensorNXT(True)
	#writeDebug(level)
	psm.screen.termPrintln(level)
	time.sleep(100)

#dinit()
psm.BBM1.brakeSync()
psm.BBM2.brakeSync()