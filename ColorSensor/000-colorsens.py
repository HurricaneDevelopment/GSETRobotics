import Rpi as rpi

rpi.init()	# Rpi initialization routine
psm = rpi.psm	# Get PiStorms

while (not psm.isKeyPressed()):
	color = psm.BAS1.colorSensorNXT()
	print color

rpi.dinit() # Rpi deinitialize routine
alias piload='function _piload(){ cp "$1" "/home/pi/PiStorms/programs/02-Student_Programs/$1"; };_piload'