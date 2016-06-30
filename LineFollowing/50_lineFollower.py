from PiStorms import PiStorms
import time
import datetime

psm = PiStorms()
debugString = ""

def writeDebug( str ):
	debugString += str + "\n"

def dinit():
	target = open("/var/robolog/" + datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S"),'w+');

writeDebug("===Starting Program===");
psm.BBM1.setSpeedSync(50)

while(not psm.isKeyPressed())
	writeDebug(psm.BAS1)
	sleep(50)

psm.BBM1.brakeSync()
psm.BBM2.brakeSync()

dinit()