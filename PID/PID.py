class PID(Object):
	def __init__(self,target,PGain,IGain,DGain,IMin,IMax,input = 0,OMin = -1000,OMax = 1000):
		setGain(PGain,IGain,DGain)
		setPoint(Target)
		setIMin(IMin)
		setIMax(IMax)
		setOMin(OMin)
		setOMax(OMax)
		self.iState = 0
		self.dState = input

	def setPGain(gain):
		self.pGain = gain
	def setIGain(gain):
		self.iGain = gain
	def setDGain(gain):
		self.dGain = gain
	def setGain(pGain,iGain,dGain):
		setPGain(pGain)
		setIGain(iGain)
		setDGain(dGain)

	def setIMax(max):
		sellf.iMax = max
	def setIMin(min):
		sellf.iMin = min
	def setOMax(max):
		sellf.oMax = max
	def setOMin(min):
		sellf.oMin = min

	def setPoint(target):
		self.setpoint = target

	def reset(input = 0):
		self.iState = 0
		self.dState = input

	def calculate(input):
		error = input - self.setpoint
		pTerm = pGain * error
		self.iState += error
		iTerm = iGain * self.iState
		iTerm = sel.iMax if self.iState > self.iMax else self.iMin if self.iState < self.iMin else iTerm
		dTerm = dGain * (input - self.dState)
		output = pTerm + iTerm + dTerm
		return sel.oMax if output > self.oMax else self.oMin if output < self.oMin else output