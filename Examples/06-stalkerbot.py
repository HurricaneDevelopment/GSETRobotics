from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

#exit variable will be used later to exit the program and return to PiStorms
exit = False

dist1=psm.BAS1.distanceUSEV3()
dist2=dist1
dist3=dist1
dist4=dist1

while(not exit):
  dist=psm.BAS1.distanceUSEV3()
  distavg=(dist+dist1+dist2+dist3+dist4)/5
  dist4=dist3
  dist3=dist2
  dist2=dist1
  dist1=dist
  if distavg>350:
     psm.BBM1.setSpeedSync(-100)
  elif distavg<250:
     psm.BBM1.setSpeedSync(100)
  elif (distavg>290 and distavg<310):
     psm.BBM1.float()
     psm.BBM2.float()
  else:
     psm.BBM1.setSpeedSync(-2*(dist-300))
  sleep(0.05)
     
  if(psm.isKeyPressed() == True): # if the GO button is pressed
    psm.screen.clearScreen()
    psm.screen.termPrintln("")
    psm.screen.termPrintln("Exiting to menu")
    psm.BBM1.float()
    psm.BBM2.float()
    sleep(0.5)
    exit = True



