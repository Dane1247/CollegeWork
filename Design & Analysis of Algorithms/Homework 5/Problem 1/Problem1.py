class Node:
	def __init__(self, isPassableBool, nodePos):
		self.isPassable = isPassableBool
		self.nodeIndex = nodePos
		self.adjList = list()
		
	def addEdge(self, targetNodePos): 
		self.adjList.append(targetNodePos)
		
def createGraph(gridList):
	gridSize = len(gridList)
	for i in range(len(gridList)):
		for j in range(len(gridList)):
			for y in range(i - 1, i + 2):
				for x in range(j - 1, j + 2):
					if not(i == y and j == x) and ((x >= 0) and (x < gridSize)) and ((y>= 0) and (y < gridSize)) and \
					gridList[i][j].isPassable and gridList[y][x].isPassable:
						#print("Adding Edge From: " + str([i, j]) + "; To: "+ str([y, x]))
						gridList[i][j].addEdge([y, x])

def findListIndex(visitedList, location):
	for i in range(len(visitedList)):
		if (visitedList[i][1] == location):
			return i

def findMinIndex(distanceList, visitedList):	
	currentMinValue = 1000
	currentMinIndex = 0
	for i in range(len(distanceList)):
		if (distanceList[i] < currentMinValue) and not(visitedList[i][0]):
			currentMinValue = distanceList[i]
			currentMinIndex = i
	return currentMinIndex

def dijikstra(nodeList, startNode, targetNode):
	visitedList = list()
	distanceList = list()
	for i in range(len(nodeList)):
		for j in range(len(nodeList[i])):
			if nodeList[i][j].isPassable:
				if [i, j] == startNode:
					distanceList.append(0)
					visitedList.append([False, [i, j], 0])
				else:
					distanceList.append(1000)
					visitedList.append([False, [i, j], 0])
	#print(distanceList)
	#print(visitedList)
	allNodesVisited = False
	while not(allNodesVisited):
		index = findMinIndex(distanceList, visitedList)
		visitedList[index][0] = True
		currentNode = nodeList[visitedList[index][1][0]][visitedList[index][1][1]]
		#print("CurrentNode: ", end = "")
		#print([visitedList[index][1][0], visitedList[index][1][1]])
		#print("adjList: ", end = "")
		#print(currentNode.adjList)
		for i in range(len(currentNode.adjList)):
			currentNodeIndex = findListIndex(visitedList, currentNode.adjList[i])
			if (distanceList[index] + 1 < distanceList[currentNodeIndex]):
				#print(visitedList[currentNodeIndex][1], end = '')
				#print(" Distance Reassighned To: " + str(distanceList[index] + 1))
				distanceList[currentNodeIndex] = distanceList[index] + 1
				visitedList[currentNodeIndex][0] = False
		allNodesVisited = True
		for i in range(len(visitedList)):
			if not(visitedList[i][0]):
				allNodesVisited = False
	print(str(distanceList[findListIndex(visitedList, targetNode)]))
	
def main():
	graphDimensions = int(input())
	startingIndex = input().split(" ")
	for i in range(len(startingIndex)):
		startingIndex[i] = int(startingIndex[i])
	endingIndex = input().split(" ")
	for i in range(len(startingIndex)):
		endingIndex[i] = int(endingIndex[i])
	gridList = list()
	for i in range(graphDimensions):
		gridList.append(list())
	for i in range(len(gridList)):
		inputList = input().split(" ")
		for j in range(len(inputList)):
			if inputList[j] == "O":
				gridList[i].append(Node(True, [i, j]))
			elif inputList[j] == "X":
				gridList[i].append(Node(False, [i, j]))
	createGraph(gridList)
	#for i in range(len(gridList)):
		#for j in range(len(gridList[i])):
			#print(gridList[i][j].isPassable, end = '')
			#print(", ", end = '')
			#print(gridList[i][j].nodeIndex, end = '')
			#print(", ", end = '')
			#print(gridList[i][j].adjList, end = '')
			#print(" ; ", end = '')
		#print()
	#print("Starting Index: ", end = '')
	#print(startingIndex)
	#print("Ending Index: ", end = '')
	#print(endingIndex)
	dijikstra(gridList, startingIndex, endingIndex)

main()