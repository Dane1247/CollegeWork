class Graph: 
	def __init__(self, numVerticesInput):
		self.nodes = [None] * numVerticesInput
		self.adjList = list()
		for i in range(numVerticesInput):
			self.adjList.append([])
		self.numVerticies = numVerticesInput
		self.inDegreeList = [0]*numVerticesInput

	def addEdge(self, souceNode, targetNode): 
		self.adjList[souceNode].append(targetNode) 
	
	def updateInDegreeList(self):
		for i in range(len(self.inDegreeList)):
			self.inDegreeList[i] = 0
		for i in range(len(self.adjList)):
			for j in range(len(self.adjList[i])):
				self.inDegreeList[self.adjList[i][j]] += 1
		
	def checkCycle(self):
		khansQueue = list()
		visitedNodes = list()
		self.updateInDegreeList()
		for i in range(len(self.inDegreeList)):
			if self.inDegreeList[i] == 0:
				khansQueue.insert(0, i)
		while len(khansQueue) > 0:
			currentNodeIndex = khansQueue.pop()
			visitedNodes.append(currentNodeIndex)
			for i in range(len(self.adjList[currentNodeIndex])):
				self.inDegreeList[self.adjList[currentNodeIndex][i]] -= 1
				if self.inDegreeList[self.adjList[currentNodeIndex][i]] <= 0:
					khansQueue.insert(0, self.adjList[currentNodeIndex][i])
		if len(visitedNodes) != len(self.nodes):
			print("Cycle!")
		else:
			print("No Cycle!")
		

def createGraph(locationsList, edgesList):
	returnGraph = Graph(len(locationsList))
	for i in range(len(locationsList)):
		returnGraph.nodes[i] = locationsList[i]
	for i in range(len(edgesList)):
		returnGraph.addEdge(edgesList[i][0], edgesList[i][1])
	return returnGraph
	
def main():
	numNodes = int(input(""))
	inputList = list()
	for i in range(numNodes):
		inputList.append(input(""))
	edgesList = list()
	numEdges = int(input("").split(" ")[1])
	for i in range(numEdges):
		currentEdge = input("").split(" ")
		for j in range(len(currentEdge)):
			currentEdge[j] = int(currentEdge[j])
		edgesList.append(currentEdge)
	createGraph(inputList, edgesList).checkCycle()

main()