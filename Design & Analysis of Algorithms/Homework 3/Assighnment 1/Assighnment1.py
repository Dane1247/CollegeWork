class TreeNode(): 
	def __init__(self, inputNodeList):
		self.nodeKeyValue = inputNodeList
		self.leftNode = None
		self.rightNode = None
		self.nodeHeight = 1
		
class AVLTreeClass():
	def __init__(self):
		self.rootNode = None
		
	def insert(self, insertNodeList):
		self.rootNode = self.insertRecursive(insertNodeList, self.rootNode)
		
	def deleteValue(self, deleteKeyValue):
		self.rootNode = self.deleteValueRecursive(deleteKeyValue, self.rootNode)
		
	def insertRecursive(self, insertNodeList, currentNode):
		if currentNode == None:
			return TreeNode(insertNodeList) 
		elif insertNodeList[0] < currentNode.nodeKeyValue[0]: 
			currentNode.leftNode = self.insertRecursive(insertNodeList, currentNode.leftNode)
		else: 
			currentNode.rightNode = self.insertRecursive(insertNodeList, currentNode.rightNode)
		currentNode.nodeHeight = 1 + max(self.getHeight(currentNode.leftNode), self.getHeight(currentNode.rightNode))
		balanceVal = self.getBalance(currentNode) 
		if balanceVal > 1 and insertNodeList[0] < currentNode.leftNode.nodeKeyValue[0]: 
			return self.rotateRight(currentNode) 
		if balanceVal < -1 and insertNodeList[0] > currentNode.rightNode.nodeKeyValue[0]: 
			return self.rotateLeft(currentNode) 
		if balanceVal > 1 and insertNodeList[0] > currentNode.leftNode.nodeKeyValue[0]: 
			currentNode.leftNode = self.rotateLeft(currentNode.leftNode) 
			return self.rotateRight(currentNode) 
		if balanceVal < -1 and insertNodeList[0] < currentNode.rightNode.nodeKeyValue[0]: 
			currentNode.rightNode = self.rotateRight(currentNode.rightNode) 
			return self.rotateLeft(currentNode) 
		return currentNode
	
	def deleteValueRecursive(self, deleteKeyValue, currentNode):
		if currentNode == None:
			return currentNode
		elif deleteKeyValue < currentNode.nodeKeyValue[0]:
			currentNode.leftNode = self.deleteValueRecursive(deleteKeyValue, currentNode.leftNode)
		elif deleteKeyValue > currentNode.nodeKeyValue[0]:
			currentNode.rightNode = self.deleteValueRecursive(deleteKeyValue, currentNode.rightNode)
		else:
			childNodeCount = 0
			if currentNode.leftNode != None:
				leftNodeExists = True
				childNodeCount += 1
			else:
				leftNodeExists = False
			if currentNode.rightNode != None:
				rightNodeExists = True
				childNodeCount += 1
			else:
				rightNodeExists = False
			if childNodeCount > 0:
				if childNodeCount == 1:
					if rightNodeExists:
						tempNode = currentNode.rightNode
						currentNode = None
						return tempNode
					elif leftNodeExists:
						tempNode = currentNode.leftNode
						currentNode = None
						return tempNode
				elif childNodeCount == 2:
					if currentNode.leftNode != None:
						tempNode = self.getLeftMostNode(currentNode.rightNode)
					elif currentNode.rightNode != None:
						tempNode = self.getRightMostNode(currentNode.leftNode)
					currentNode.nodeKeyValue = tempNode.nodeKeyValue
					currentNode.rightNode = self.deleteValueRecursive(tempNode.nodeKeyValue[0], currentNode.rightNode)
			else:
				currentNode = None
				return currentNode
		if currentNode == None:
			return currentNode
		currentNode.nodeHeight = 1 + max(self.getHeight(currentNode.leftNode), self.getHeight(currentNode.rightNode))
		balanceVal = self.getBalance(currentNode) 
		if balanceVal > 1 and deleteKeyValue < currentNode.leftNode.nodeKeyValue[0]: 
			return self.rotateRight(currentNode) 
		if balanceVal < -1 and deleteKeyValue > currentNode.rightNode.nodeKeyValue[0]: 
			return self.rotateLeft(currentNode) 
		if balanceVal > 1 and deleteKeyValue > currentNode.leftNode.nodeKeyValue[0]: 
			currentNode.leftNode = self.rotateLeft(currentNode.leftNode) 
			return self.rotateRight(currentNode) 
		if balanceVal < -1 and deleteKeyValue < currentNode.rightNode.nodeKeyValue[0]: 
			currentNode.rightNode = self.rotateRight(currentNode.rightNode) 
			return self.rotateLeft(currentNode) 
		return currentNode
		
	def getLeftMostNode(self, currentNode):
		if (currentNode.leftNode == None):
			return currentNode
		return self.getLeftMostNode(currentNode.leftNode)
		
	def getRightMostNode(self, currentNode):
		if (currentNode.rightNode == None):
			return currentNode
		return self.getRightMostNode(currentNode.rightNode)

	def getValue(self, searchValue):
		self.valueFound = False
		self.getValueRecursive(self.rootNode, searchValue)
		if not(self.valueFound):
			print("Not Found")
		
	def getValueRecursive(self, currentNode, searchValue):
		if (currentNode.nodeKeyValue[0] == searchValue):
			print(str(currentNode.nodeKeyValue[1]))
			self.valueFound = True
			return None
		if (currentNode.leftNode != None) and not(self.valueFound):
			valueFound = self.getValueRecursive(currentNode.leftNode, searchValue)
		if (currentNode.rightNode != None) and not(self.valueFound):
			valueFound = self.getValueRecursive(currentNode.rightNode, searchValue)
		
	def rotateLeft(self, inputNode):
		returnNode = inputNode.rightNode 
		newLeftNode = returnNode.leftNode 
		returnNode.leftNode = inputNode 
		inputNode.rightNode = newLeftNode
		inputNode.nodeHeight = 1 + max(self.getHeight(inputNode.leftNode), self.getHeight(inputNode.rightNode)) 
		returnNode.nodeHeight = 1 + max(self.getHeight(returnNode.leftNode), self.getHeight(returnNode.rightNode)) 
		return returnNode 
		
	def rotateRight(self, inputNode): 
		returnNode = inputNode.leftNode 
		newRightNode = returnNode.rightNode 
		returnNode.rightNode = inputNode 
		inputNode.leftNode = newRightNode
		inputNode.nodeHeight = 1 + max(self.getHeight(inputNode.leftNode), self.getHeight(inputNode.rightNode)) 
		returnNode.nodeHeight = 1 + max(self.getHeight(returnNode.leftNode), self.getHeight(returnNode.rightNode)) 
		return returnNode 
  
	def getHeight(self, inputNode): 
		if not inputNode:
			return 0
		return inputNode.nodeHeight 
  
	def getBalance(self, inputNode): 
		if not inputNode:
			return 0
		return self.getHeight(inputNode.leftNode) - self.getHeight(inputNode.rightNode) 
			
	def getTreeHeight(self, rootNode): 
		if rootNode == None:
			return 0
		else : 
			lTreeheight = self.getHeight(rootNode.leftNode)
			rTreeheight = self.getHeight(rootNode.rightNode) 
			if lTreeheight > rTreeheight : 
				return lTreeheight + 1
			else: 
				return rTreeheight + 1
				
	def levelOrder(self, rootNode):
		treeHeight = self.getTreeHeight(rootNode)
		for i in range(1, treeHeight + 1): 
			self.printCurrentLevel(rootNode, i)
		print()
			
	def printCurrentLevel(self, inputNode, currentLevel):
		if inputNode == None: 
			return None
		if currentLevel == 1: 
			print(str(inputNode.nodeKeyValue[0]) + ":" + inputNode.nodeKeyValue[1] + "(" + str(self.getBalance(inputNode)) + ")", end = ' ')
		elif currentLevel > 1 : 
			self.printCurrentLevel(inputNode.leftNode , currentLevel - 1) 
			self.printCurrentLevel(inputNode.rightNode , currentLevel - 1) 
			
def main():
	numCommands = int(input())
	treeObject = AVLTreeClass()
	for i in range(numCommands):
		userInput = input().split(" ")
		if userInput[0] == "put":
			treeObject.insert([int(userInput[1]), userInput[2]])
		if userInput[0] == "get":
			treeObject.getValue(int(userInput[1]))
		if userInput[0] == "remove":
			treeObject.deleteValue(int(userInput[1]))
		if userInput[0] == "levelorder":
			treeObject.levelOrder(treeObject.rootNode)		
			

main()