class PID(object):
	def __init__(self,target,PGain,IGain,DGain,IMin,IMax,input = 0,OMin = -1000,OMax = 1000,iResetMin = 0,iResetMax = 0):
		self.setGains(PGain,IGain,DGain)
		self.setPoint(target)
		self.setIMin(IMin)
		self.setIMax(IMax)
		self.setOMin(OMin)
		self.setOMax(OMax)
		self.iState = 0
		self.dState = input

	def setPGain(self,gain):
		self.pGain = gain
	def setIGain(self,gain):
		self.iGain = gain
	def setDGain(self,gain):
		self.dGain = gain
	def setGains(self,pGain,iGain,dGain):
		self.setPGain(pGain)
		self.setIGain(iGain)
		self.setDGain(dGain)

	def setIMax(self,max):
		self.iMax = max
	def setIMin(self,min):
		self.iMin = min
	def setOMax(self,max):
		self.oMax = max
	def setOMin(self,min):
		self.oMin = min
	def iResetMin(self,min):
		self.iResetMin = min
	def iResetMax(self,max):
		self.iResetMax = max

	def setPoint(self,target):
		self.setpoint = target

	def reset(self,input = 0):
		self.iState = 0
		self.dState = input

	def calculate(self,input):
		error = input - self.setpoint
		pTerm = self.pGain * error
		self.iState += error
		self.iState = self.iMax if self.iState > self.iMax else (self.iMin if self.iState < self.iMin else self.iState)
		self.iState = (0 if error <= self.iResetMax and error >= self.iResetMin else self.iState) if self.iResetMin != 0 and self.iResetMax != 0 else self.iState
		iTerm = self.iState * self.iGain
		dTerm = self.dGain * (input - self.dState)
		self.dState = input
		output = pTerm + iTerm + dTerm
		#print '%f\t%f\t%f\t%f' % (pTerm,iTerm,dTerm,output)
		return self.oMax if output > self.oMax else (self.oMin if output < self.oMin else output)
