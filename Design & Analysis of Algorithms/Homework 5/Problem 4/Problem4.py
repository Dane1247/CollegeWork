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
	currentMinIndex = -1
	for i in range(len(distanceList)):
		if (distanceList[i] < currentMinValue) and not(visitedList[i]):
			currentMinValue = distanceList[i]
			currentMinIndex = i
	return currentMinIndex
	
def findNodeIndex(nodeList, nodeName):
	for i in range(len(nodeList)):
		if nodeList[i][0] == nodeName:
			return i
	return -1
	
def printDistanceList(distanceList, nodeList, establishedRoutesList):
	alphabetizedList = list()
	for i in range(len(establishedRoutesList)):
		alphabetizedList.append(establishedRoutesList[i][0])
	alphabetizedList = sorted(alphabetizedList)
	for i in range(len(alphabetizedList)):
		calculatedDistance = distanceList[findNodeIndex(nodeList, alphabetizedList[i])]
		establishedDistance = int(establishedRoutesList[findNodeIndex(establishedRoutesList, alphabetizedList[i])][1])
		if calculatedDistance == 100000:
			print(alphabetizedList[i] + " NO PATH")
		elif calculatedDistance >= establishedDistance:
			print(alphabetizedList[i] + " FASTEST")
		else:
			print(alphabetizedList[i] + " " + str(establishedDistance - calculatedDistance))
	
def dijikstra(nodeList, startLocation, establishedRoutesList):
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
	#print(visitedList)
	#print(distanceList)
	while not(allNodesVisited):
		index = findMinIndex(distanceList, visitedList)
		visitedList[index]= True
		#print("Current Node: ", end = '')
		#print(nodeList[index])
		#print(index)
		for i in range(len(nodeList[index][1])):
			#print("Current Adj Node: ", end = '')
			#print(nodeList[nodeList[index][1][i][0]][0])
			currentNodeIndex = nodeList[index][1][i][0]
			currentEdgeWeight = nodeList[index][1][i][1]
			#print("CurrentEdgeWeight: ", end = '')
			#print(currentEdgeWeight)
			if ((distanceList[index] + currentEdgeWeight) < distanceList[currentNodeIndex]):
				#print("weightUpdated")
				distanceList[currentNodeIndex] = distanceList[index] + currentEdgeWeight
				visitedList[currentNodeIndex] = False
		allNodesVisited = True
		for i in range(len(visitedList)):
			if not(visitedList[i]):
				allNodesVisited = False
		if index == -1:
			allNodesVisited = True
	printDistanceList(distanceList, nodeList, establishedRoutesList)
	
def main():
	startingNodeValue = input("")
	numEstablishedRoutes = int(input())
	establishedRoutesList = list()
	for i in range(numEstablishedRoutes):
		establishedRoutesList.append(input("").split(","))
		for j in range(len(establishedRoutesList[i])):
			establishedRoutesList[i][j] = establishedRoutesList[i][j].strip(" ")		
	inputList = list()
	numEdges = int(input(""))
	for i in range(numEdges):
		inputList.append(input("").split(","))
		for j in range(len(inputList[i])):
			inputList[i][j] = inputList[i][j].strip(" ")
	graphObject = createGraph(inputList)
	dijikstra(graphObject.nodes, startingNodeValue, establishedRoutesList)

main()