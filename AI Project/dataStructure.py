from sklearn import preprocessing
from dataIO import dataIO

class dataStructure:
	def __init__(self):
		self.dataIO = [dataIO.datamanager]

	def append(self, newVal):
		self.dataIO.append(newVal)

	def toArray(self):
		return self.dataIO

	def size(self):
		return len(self.dataIO)

	def normalize(self):
		return preprocessing.scale(self.dataIO)