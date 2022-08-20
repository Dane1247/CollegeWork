class Node:
    def __init__(self, value, leftNode = None, rightNode = None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode

class BinaryTree:
	def __init__(self, root = None):
		self.rootNode = root

	def fromArray(self, sourceArray, index = 0, rootNode = None):
		if index < len(sourceArray):
			rootNode = Node(sourceArray[index])
			rootNode.leftNode = self.fromArray(sourceArray, (2 * index) + 1, rootNode.leftNode)
			rootNode.rightNode = self.fromArray(sourceArray, (2 * index) + 2, rootNode.rightNode)
		self.rootNode = rootNode
		return rootNode

	def toArray(self, numNodes, rootNode, index = 0, returnArray = None):
		if index == 0:
			returnArray = [0]*numNodes
		if rootNode != None:
			returnArray[index] = rootNode.value
			self.toArray(numNodes, rootNode.leftNode, (2 * index) + 1, returnArray)
			self.toArray(numNodes, rootNode.rightNode, (2 * index) + 2, returnArray)
		return returnArray
	
	def isBST(self, currentNode):
		if currentNode != None:
			if currentNode.leftNode != None:
				if currentNode.leftNode.value > currentNode.value:
					return False
			if currentNode.rightNode != None:
				if currentNode.rightNode.value < currentNode.value:
					return False
			self.isBST(currentNode.leftNode)
			self.isBST(currentNode.rightNode)
			return True
	
	def preOrder(self, currentNode):
		if currentNode != None:
			print(str(currentNode.value) + " ", end = '')
			self.preOrder(currentNode.leftNode)
			self.preOrder(currentNode.rightNode)
		
	def postOrder(self, currentNode):
		if currentNode != None:
			self.postOrder(currentNode.leftNode)
			self.postOrder(currentNode.rightNode)
			print(str(currentNode.value) + " ", end = '')
	
	def numNodesInLookup(self, numNodes, searchValue):
		if self.isBST(self.rootNode):
			self.BSTSearch(self.rootNode, searchValue)
		else:
			self.inOrderSearch(numNodes, self.rootNode, searchValue)
	
	def BSTSearch(self, rootNode, searchValue, numNodesInLookup = 0):
		if rootNode != None:
			numNodesInLookup += 1
			if rootNode.value == searchValue:
				print(str(numNodesInLookup))
				return True
			elif searchValue < rootNode.value:
				self.BSTSearch(rootNode.leftNode, searchValue, numNodesInLookup)
			elif searchValue > rootNode.value:
				self.BSTSearch(rootNode.rightNode, searchValue, numNodesInLookup)
		
	def inOrderSearch(self, numNodes, rootNode, searchValue, numNodesInLookup = 0):
		treeArray = self.toArray(numNodes, self.rootNode)
		for i in range(len(treeArray)):
			numNodesInLookup += 1
			if treeArray[i] == searchValue:
				print(str(numNodesInLookup))
				return True
		
def main():
	numNodes = int(input(""))
	nodeValues = input("").split(" ")
	treeArray = list()
	for i in range(len(nodeValues)):
		treeArray.append(int(nodeValues[i]))
	treeClass = BinaryTree()
	treeClass.fromArray(treeArray)
	numInputs = int(input(""))
	for i in range(numInputs):
		userInput =  input("").split(" ")
		if userInput[0] == "toArray":
			treeArray = treeClass.toArray(numNodes, treeClass.rootNode)
			for i in range(len(treeArray)):
				if i < len(treeArray) - 1:
					print(str(treeArray[i]) + " ", end = '')
				else:
					print(str(treeArray[i]), end = '')
			print()
		elif userInput[0] == "isBST":
			if treeClass.isBST(treeClass.rootNode):
				print("True")
			else:
				print("False")
		elif userInput[0] == "preOrder":
			treeClass.preOrder(treeClass.rootNode)
			print()
		elif userInput[0] == "postOrder":
			treeClass.postOrder(treeClass.rootNode)
			print()
		elif userInput[0] == "numNodesInLookup":
			treeClass.numNodesInLookup(numNodes, int(userInput[1]))
		
main()