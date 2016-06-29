from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

for x in range(0,255):
  psm.led(1,x,0,0) 
  sleep(0.05)
sleep(1.0)
psm.led(1,0,0,0)    



