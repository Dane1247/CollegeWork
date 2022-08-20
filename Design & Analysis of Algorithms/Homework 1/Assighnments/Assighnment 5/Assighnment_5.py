def returnMax(inputArray):
	currentMax = inputArray[0]
	for i in range(len(inputArray)):
		if currentMax > inputArray[i]:
			currentMax = inputArray[i]
	return currentMax
	
def returnMin(inputArray):
	currentMin = inputArray[0]
	for i in range(len(inputArray)):
		if currentMin > inputArray[i]:
			currentMin = inputArray[i]
	return currentMin

def findHighestBelow(inputArray, maxValue):
	currentMax = returnMin(inputArray)
	for i in range(len(inputArray)):
		if (inputArray[i] > currentMax) and (inputArray[i] <= maxValue):
			currentMax = inputArray[i]
	return currentMax
	
def calcCost(groupsList):
	totalValue = 0
	for i in range(len(groupsList)):
		for j in range(len(groupsList[i])):
				totalValue += groupsList[i][j]
		if len(groupsList[i]) == 3:
			totalValue -= returnMin(groupsList[i])
	return totalValue
				

def main():
	numElements = int(input(""))
	inputArray=  list()
	for i in range(numElements):
		inputArray.append(int(input("")))
	print(inputArray)
	numGroups3 = numElements//3
	remainder = numElements - numGroups3*3
	groups3List = list()
	print(numGroups3)
	for i in range(numGroups3):
		groups3List.append([])
	if remainder > 0:
		groups3List.append([])
		for i in range(remainder):
			targetIndex = inputArray.index(returnMin(inputArray))
			groups3List[numGroups3].append(inputArray[targetIndex])
			inputArray.remove(inputArray[targetIndex])
		for i in range(numGroups3):
			for j in range(2):
				targetIndex = inputArray.index(returnMax(inputArray))
				groups3List[i].append(inputArray[targetIndex])
				inputArray.remove(inputArray[targetIndex])
		for i in range(numGroups3):
			targetIndex = inputArray.index(findHighestBelow(inputArray, returnMin(groups3List[i])))
			groups3List[i].append(inputArray[targetIndex])
			inputArray.remove(inputArray[targetIndex])
	else:
		for i in range(numGroups3):
			for j in range(2):
				targetIndex = inputArray.index(returnMax(inputArray))
				groups3List[i].append(inputArray[targetIndex])
				inputArray.remove(inputArray[targetIndex])
		for i in range(numGroups3):
			targetIndex = inputArray.index(findHighestBelow(inputArray, returnMin(groups3List[i])))
			groups3List[i].append(inputArray[targetIndex])
			inputArray.remove(inputArray[targetIndex])
	print(groups3List)
	print(calcCost(groups3List))

main()