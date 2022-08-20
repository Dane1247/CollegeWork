def searchForNames(searchNamesList, inputArray):
	arrayMidpoint = (len(inputArray)//2) - 1
	for i in range(len(searchNamesList)):
		numNamesScanned = 0
		resultIndex = -1
		stopScannCounting = False
		if searchNamesList[i][0] < 'M':
			for j in range(arrayMidpoint, -1, -1):
				if (not(stopScannCounting)):
					numNamesScanned += 1
				if searchNamesList[i] == inputArray[j][0]:
					resultIndex = j
					stopScannCounting = True
		else:
			for j in range(arrayMidpoint + 1, len(inputArray), 1):
				if (not(stopScannCounting)):
					numNamesScanned += 1
				if searchNamesList[i] == inputArray[j][0]:
					resultIndex = j
					stopScannCounting = True
		print(str(resultIndex) + ": " + str(numNamesScanned))
					
				
def main():
	numElements = int(input(""))
	inputArray=  list()
	for i in range(numElements):
		inputArray.append(input("").split(" "))
	numNames = int(input(""))
	searchNamesList = list()
	for i in range(numNames):
		searchNamesList.append(input(""))
	searchForNames(searchNamesList, inputArray)
	

main()