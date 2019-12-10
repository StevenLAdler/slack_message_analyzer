import json
class GetConfig(object):
	def __init__(self):
		self.start = ""
		self.end = ""
		self.inc = ""
		self.cont = False
		self.path = ""
		self.channels = []
		
	def getStart(self):
		return self.start
		
	def setStart(self, start):
		self.start = start
		
	def getEnd(self):
		return self.end
		
	def setEnd(self, end):
		self.end = end
		
	def getIncrement(self):
		return self.inc
		
	def setIncrement(self, inc):
		self.inc = inc
		
	def getCont(self):
		return self.cont
		
	def setCont(self, cont):
		if cont == "True":
			self.cont = True
		elif cont == "False":
			self.cont = False
		
	def getPath(self):
		return self.path
		
	def setPath(self, path):
		self.path = path
		
	def getChannels(self):
		return self.channels
		
	def setChannels(self, channels):
		self.channels = channels
		
	#def validateInput(self):
		
	def readJson(self):
		with open('config.json') as config_file:
			data = json.load(config_file)
		self.setStart(data['start'])
		self.setEnd(data['end'])
		#can be set to 'day', 'week', 'month'. increment of each data point.
		self.setIncrement(data['increment']) 
		#continue to nearest full increment?
		self.setCont(data['cont'])
		self.setPath(data['path'])
		self.setChannels(data['channels'])
	
	def printConfig(self):
		print(self.getStart())
		print(self.getEnd())
		print(self.getIncrement())
		print(self.getCont())
		print(self.getPath())
		print(self.getChannels())