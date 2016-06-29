from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

#exit variable will be used later to exit the program and return to PiStorms
exit = False

while(not exit):
  dist=psm.BAS1.distanceUSEV3()
  if dist>200:
     psm.BBM1.setSpeed(-100)
     psm.BBM2.setSpeed(-100)
  else:
     psm.BBM1.setSpeed(100)
     psm.BBM2.setSpeed(100)
  sleep(0.05)
     
  if(psm.isKeyPressed() == True): # if the GO button is pressed
    psm.screen.clearScreen()
    psm.screen.termPrintln("")
    psm.screen.termPrintln("Exiting to menu")
    psm.BBM1.setSpeed(0)
    psm.BBM2.setSpeed(0)
    sleep(0.5)
    exit = True



