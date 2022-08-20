class Graph: 
	def __init__(self, numVerticesInput):
		alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		self.nodes = alphabetList[:numVerticesInput]
		self.adjList = list()
		for i in range(numVerticesInput):
			self.adjList.append([])
		self.numVerticies = numVerticesInput

	def addEdge(self, souceNode, targetNode): 
		self.adjList[souceNode].append(targetNode) 
		
	def topologicalSortUtil(self, currentNode, visitedNodes, valueStack): 
		visitedNodes[currentNode] = True
		for i in self.adjList[currentNode]: 
			if visitedNodes[i] == False: 
				self.topologicalSortUtil(i, visitedNodes, valueStack) 
		valueStack.insert(0, self.nodes[currentNode])
		
	def topologicalSort(self): 
		visitedNodes = [False]*self.numVerticies
		valueStack =[] 
		for i in range(self.numVerticies): 
			if visitedNodes[i] == False: 
				self.topologicalSortUtil(i, visitedNodes, valueStack) 
		for i in range(len(valueStack) - 1):
			print(valueStack[i] + " ")
		print(valueStack[len(valueStack) - 1])
		
def sortAlpha(inputList):
	letterGraph = Graph(findNumLetters(inputList))
	for i in range(len(inputList) - 1):
		mismatchFound = False
		j = 0
		while not(mismatchFound) and (j < min(len(inputList[i]), len(inputList[i + 1]))):
			if inputList[i][j] != inputList[i + 1][j]:
				letterGraph.addEdge(letterGraph.nodes.index(inputList[i][j]), letterGraph.nodes.index(inputList[i + 1][j]))
				mismatchFound = True
			else:
				j += 1
	letterGraph.topologicalSort()
		
def findNumLetters(wordList):
	largestLetter = 'a'
	for i in range(len(wordList)):
		for j in range(len(wordList[i])):
			if wordList[i][j] > largestLetter:
				largestLetter = wordList[i][j]
	return ord(largestLetter) - ord('a') + 1
	
def main():
	numWords = int(input(""))
	inputList = list()
	for i in range(numWords):
		inputList.append(input(""))
	sortAlpha(inputList)

main()