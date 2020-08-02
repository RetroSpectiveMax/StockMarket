import numpy as np

###LOBF###


# xAxis = [0, 1, 2, 3]
# yAxis = [0, 2, 6, 13]

#user_input = int(input("What x value do you want to figure out? "))


def mean(data):
	total = 0
	for x in range(len(data)):
		total += data[x]
	return float(total) / len(data)

def multiply(data1, data2):
	tempArray = []
	for x in range(len(data1)):
		tempArray.append(data1[x] * data2[x])
	return tempArray

def squareArray(data):
	tempArray = []
	for x in range(len(data)):
		tempArray.append(data[x] ** 2)
	return tempArray

#Slope#
def lineOfBestFit(data1, data2):
	
	#calculate components of LOBF#
	aveOfArray = mean(data1) * mean(data2)
	multArray = mean(multiply(data1, data2))
	squareAve = mean(data1) * mean(data1)
	aveSquared = mean(squareArray(data1))

	
	#Piece together equation#
	m = (aveOfArray - multArray) / (squareAve - aveSquared)
	return m

#lineOfBestFit(xAxis, yAxis) 


def yIntercept(x, y):
	b = mean(y) - (lineOfBestFit(x, y) * mean(x))
	return b

#yIntercept(xAxis, yAxis)

def findExactVal(input, x, y):
	slope = lineOfBestFit(x, y) * input
	line = slope + yIntercept(x, y)
	print(line)
	return line

#findExactVal(user_input, xAxis, yAxis)

###Analyzing Previous Data###

x = [0, 1, 2, 3, 4]
y = [0, 2, 5, 13, 21]

spikeX = []

def checkForSpike(x, y):
	prevTerm = 0
	term = 0
	yr = 0
	for x in range(len(y)):
		term = y[x]
		if(prevTerm + 5 <= term):
			#print(x)
			return x
		prevTerm = term

#checkForSpike(xAxis, yAxis)

def findXforSpike(x, y):
	point = checkForSpike(x, y)
	xPoint = x[point]
	print(xPoint)
	spikeX.append(xPoint)
	return xPoint

findXforSpike(x, y)




