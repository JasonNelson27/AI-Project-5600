from sklearn import linear_model
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from sklearn.ensemble import RandomForestRegressor
from dataStructure import dataStructure


techInd = 20

class changePredictor:
	def __init__(self):
		self.predictor = "prediction"
		self.data = dataStructure()

class neuralNetworkChangePredictor(changePredictor):
	def __init__(self):
		self.data = dataStructure()
		self.prevValue = 0;

	def predict(self, currentData):
		if len(self.data.toArray()) < techInd:
			self.data.append(currentData)
			return

		net = buildNetwork(len(currentData),3,2)
		dataset = SupervisedDataSet(len(currentData), 1)
		#-------------training ----------------
		tempArr = self.data.toArray()[self.data.size()-techInd:self.data.size()]
		for index in range(0, len(tempArr)-1):
			dataset.addSample(tuple(tempArr[index]), tempArr[index+1][0])
		trainer = BackpropTrainer(net, dataset)
		trainer.trainEpochs(5000)
		prediction = net.activate(tuple(currentData))
		#------------------------------------
		
		self.data.append(currentData)
		prediction = prediction[0]
		if prediction = 0: 
			prediction = (currentData[0]/prediction)
		if prediction = 1: 
			prediction = (currentData[0]/prediction)-1
		return prediction
