class Graph: 
	def __init__(self):
		self.nodes = list()

	def addEdge(self, souceNodeName, targetNodeName, edgeWeight):
		sourceIndex = self.findIndexNode(souceNodeName)
		targetIndex = self.findIndexNode(targetNodeName)
		self.nodes[sourceIndex][1].append([targetIndex, edgeWeight])
		
	def findIndexNode(self, nodeName):
		for i in range(len(self.nodes)):
			if self.nodes[i][0] == nodeName:
				return i
		self.nodes.append([nodeName, list()])
		return len(self.nodes) - 1

def createGraph(inputList):
	returnGraph = Graph()
	for i in range(len(inputList)):
		returnGraph.addEdge(inputList[i][0], inputList[i][1], int(inputList[i][2]))
	return returnGraph
	
def findMinIndex(distanceList, visitedList):	
	currentMinValue = 100000
	currentMinIndex = 0
	for i in range(len(distanceList)):
		if (distanceList[i] < currentMinValue) and not(visitedList[i]):
			currentMinValue = distanceList[i]
			currentMinIndex = i
	return currentMinIndex
	
def printDistanceList(distanceList, nodeList):
	alphabetizedList = list()
	standardOrderedList = list()
	for i in range(len(nodeList)):
		alphabetizedList.append(nodeList[i][0])
		standardOrderedList.append(nodeList[i][0])
	alphabetizedList = sorted(alphabetizedList)
	for i in range(len(alphabetizedList)):
		currentIndex = standardOrderedList.index(alphabetizedList[i])
		print(alphabetizedList[i] + ": " + str(distanceList[currentIndex]))
	
def dijikstra(nodeList, startLocation):
	visitedList = list()
	distanceList = list()
	for i in range(len(nodeList)):
			if nodeList[i][0] == startLocation:
				distanceList.append(0)
				visitedList.append(False)
			else:
				distanceList.append(100000)
				visitedList.append(False)
	allNodesVisited = False
	while not(allNodesVisited):
		index = findMinIndex(distanceList, visitedList)
		visitedList[index]= True
		for i in range(len(nodeList[index][1])):
			currentNodeIndex = nodeList[index][1][i][0]
			currentEdgeWeight = nodeList[index][1][i][1]
			if ((distanceList[index] + currentEdgeWeight) < distanceList[currentNodeIndex]):
				distanceList[currentNodeIndex] = distanceList[index] + currentEdgeWeight
				visitedList[currentNodeIndex] = False
		allNodesVisited = True
		for i in range(len(visitedList)):
			if not(visitedList[i]):
				allNodesVisited = False
	printDistanceList(distanceList, nodeList)
				
	
def main():
	startingNodeValue = input("")
	inputList = list()
	numEdges = int(input(""))
	for i in range(numEdges):
		inputList.append(input("").split(","))
		for j in range(len(inputList[i])):
			inputList[i][j] = inputList[i][j].strip(" ")
	graphObject = createGraph(inputList)
	dijikstra(graphObject.nodes, startingNodeValue)

main()