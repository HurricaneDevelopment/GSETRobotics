from PiStorms import PiStorms
from time import sleep
print "running program"
psm = PiStorms()

psm.screen.askQuestion(["Hello World" , "Press OK to Exit"],["OK"])



