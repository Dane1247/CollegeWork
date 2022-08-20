class Graph: 
	def __init__(self, numVerticesInput):
		self.nodes = [None] * numVerticesInput
		self.adjList = list()
		for i in range(numVerticesInput):
			self.adjList.append([])
		self.numVerticies = numVerticesInput

	def addEdge(self, souceNode, targetNode): 
		self.adjList[souceNode].append(targetNode) 

def createGraph(locationsList, edgesList):
	returnGraph = Graph(len(locationsList))
	for i in range(len(locationsList)):
		returnGraph.nodes[i] = locationsList[i]
	for i in range(len(edgesList)):
		returnGraph.addEdge(edgesList[i][0], edgesList[i][1])
	return returnGraph
	
def main():
	numAllowedTraversials = int(input(""))
	startingNodeValue = input("")
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
	createGraph(inputList, edgesList).possibleLocations(startingNodeValue, numAllowedTraversials)

main()