from PiStorms import PiStorms
import time
import datetime

psm = None
debugString = ""

def init():
	global psm
	writeDebug("===Starting on " + datetime.datetime.now().strftime("%D %I:%M %p"))
	psm = PiStorms()

def writeDebug( message ):
	global debugString
	debugString += str(message) + "\n"

def dinit():
	target = open("/var/robolog/" + datetime.datetime.now().strftime("%m-%d-%Y_%H-%M-%S"),'w+')
	target.write(debugString)
	target.close()

	psm.BBM1.brakeSync()
	psm.BBM2.brakeSync()
	psm.led(1,0,0,0)
	psm.led(2,0,0,0)