class Graph: 
	def __init__(self, numVerticesInput):
		self.nodes = [None] * numVerticesInput
		self.adjList = list()
		for i in range(numVerticesInput):
			self.adjList.append([])
		self.numVerticies = numVerticesInput

	def addEdge(self, souceNode, targetNode): 
		self.adjList[souceNode].append(targetNode) 
		
	def countingGraphTraversial(self, currentNodeIndex, endingNodeIndex, numNodesTraveledList, visitedNodes, currentDepth = 0):
		localVisitedListCopy = list()
		for i in range(len(visitedNodes)):
			localVisitedListCopy.append(visitedNodes[i])
		if currentNodeIndex == endingNodeIndex:
			numNodesTraveledList.append(currentDepth)
		elif not(localVisitedListCopy[currentNodeIndex]):
			localVisitedListCopy[currentNodeIndex] = True
			for i in range(len(self.adjList[currentNodeIndex])):
				self.countingGraphTraversial(self.adjList[currentNodeIndex][i], endingNodeIndex, numNodesTraveledList, localVisitedListCopy, currentDepth + 1)
			
	def findLongestRoute(self, startingNodeValue, endingNodeValue): 
		numNodesTraveledList = list()
		visitedNodes = [False]*self.numVerticies
		self.countingGraphTraversial(self.nodes.index(startingNodeValue), self.nodes.index(endingNodeValue), numNodesTraveledList, visitedNodes)
		print(max(numNodesTraveledList))
		
			
def createGraph(locationsList, edgesList):
	returnGraph = Graph(len(locationsList))
	for i in range(len(locationsList)):
		returnGraph.nodes[i] = locationsList[i]
	for i in range(len(edgesList)):
		returnGraph.addEdge(edgesList[i][0], edgesList[i][1])
	return returnGraph
	
def main():
	startingNodeValue = input("")
	endingNodeValue = input("")
	inputList = list()
	numLocations = int(input(""))
	for i in range(numLocations):
		inputList.append(input(""))
	edgesList = list()
	numEdges = int(input("").split(" ")[1])
	for i in range(numEdges):
		currentEdge = input("").split(" ")
		for j in range(len(currentEdge)):
			currentEdge[j] = int(currentEdge[j])
		edgesList.append(currentEdge)
	createGraph(inputList, edgesList).findLongestRoute(startingNodeValue, endingNodeValue)

main()