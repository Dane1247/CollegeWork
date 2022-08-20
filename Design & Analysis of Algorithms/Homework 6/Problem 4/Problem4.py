def checkClearSquare(inputArray): 
	dimensions = len(inputArray)
	arrayCopy = list()
	for i in range(len(inputArray)):
		arrayCopy.append(list())
		for j in range(len(inputArray[i])):
			arrayCopy[i].append(0)
	for i in range(1, dimensions):
		for j in range(1, dimensions):
			if (inputArray[i][j] == 1):
				arrayCopy[i][j] = min(arrayCopy[i][j-1], arrayCopy[i-1][j], arrayCopy[i-1][j-1]) + 1
			else:
				arrayCopy[i][j] = 0
	maxArrayCopy = arrayCopy[0][0] 
	maxY = 0
	maxX = 0
	for i in range(dimensions):
		for j in range(dimensions):
			if (maxArrayCopy < arrayCopy[i][j]): 
				maxArrayCopy = arrayCopy[i][j] 
				maxY = i 
				maxX = j 
	print(min(maxY, maxX))

def main():	
	graphDimensions = int(input())
	gridList = list()
	for i in range(graphDimensions):
		gridList.append(list())
	for i in range(len(gridList)):
		inputList = input().split(" ")
		for j in range(len(inputList)):
			if inputList[j] == "0":
				gridList[i].append(1)
			elif inputList[j] == "1":
				gridList[i].append(0)
	checkClearSquare(gridList)

main()