class Node():
	def __init__(self, c, freq):
		self.c = c
		self.freq = freq
		self.left = None
		self.right = None
  
class MinHeap():
	def __init__(self):
		self.data = []
  
	def empty(self):
		return self.size() == 0

	def size(self):
		return len(self.data)

	def insert(self, val):
		self.data.append(val)
		self.__heapifyUp(len(self.data) - 1)

	def extractMin(self):
		temp = self.data[0]
		self.__swap(0, -1)    
		self.data.remove(self.data[-1])
		self.__heapifyDown(0)
		return temp

	def __swap(self,i,j):
		self.data[i], self.data[j] = self.data[j], self.data[i]

	def __heapifyUp(self, idx):
		if idx > 0:
			parent = (idx - 1) // 2
			if (self.data[parent].freq > self.data[idx].freq):
				self.__swap(parent, idx)
				self.__heapifyUp(parent)
    
	def __heapifyDown(self, idx):
		data = self.data
		left = 2 * idx + 1
		right = 2 * idx + 2
		mini = idx
		if (left < len(data) and (data[left].freq < data[mini].freq)):
			mini = left
		if (right < len(data) and (data[right].freq < data[mini].freq)):
			mini = right
		if (mini is not idx):
			self.__swap(mini, idx)
			self.__heapifyDown(mini)
	  
class HuffmanTree:
	def __init__(self):
		self.nodeQueue = MinHeap()
		self.encodingDict = {}
		self.rootNode = None
		
	def combineNodes(self):
		while(len(self.nodeQueue.data) > 1):
			leftNode = self.nodeQueue.extractMin()
			rightNode = self.nodeQueue.extractMin()
			merged = Node(None, leftNode.freq  + rightNode.freq)
			merged.left = leftNode
			merged.right = rightNode
			self.nodeQueue.insert(merged)
		self.rootNode = self.nodeQueue.extractMin()
		
	def checkList(self, nodeList, checkChar):
		for i in range(len(nodeList)):
			if nodeList[i].c == checkChar:
				return True
		return False
		
	def increaseFreq(self, nodeList, incChar):
		for i in range(len(nodeList)):
			if nodeList[i].c == incChar:
				nodeList[i].freq = nodeList[i].freq + 1
		
	def populateHeap(self, charText):
		heapList = list()
		for i in range(len(charText)):
			if not(self.checkList(heapList, charText[i])):
				heapList.append(Node(charText[i], 1))
			else:
				self.increaseFreq(heapList, charText[i])
		#for i in range(len(heapList)):
		#	print(heapList[i].c + ":" + str(heapList[i].freq))
		for i in range(len(heapList)):
			self.nodeQueue.insert(heapList[i])
		
	def buildDicts(self, binaryString = "", currentNode = None):
		if currentNode == None:
			currentNode = self.rootNode
		#if currentNode.c != None:
		#	print("Current Char: " + currentNode.c)
		#print("Current Binary String: " + binaryString)
		if currentNode.left != None:
			self.buildDicts(binaryString + "0", currentNode.left)
		if currentNode.right != None:
			self.buildDicts(binaryString + "1", currentNode.right)
		if currentNode.c != None:
			self.encodingDict[currentNode.c] = binaryString
			
	def buildData(self, charText):
		self.populateHeap(charText)
		self.combineNodes()
		self.buildDicts()
		#print(self.encodingDict)
		#keyList = list(self.encodingDict)
		#valuesList = list(self.encodingDict.values())
		#print(keyList)
		#print(valuesList)
		
	def printEncodedString(self, charText):
		binaryString = ""
		for i in range(len(charText)):
			binaryString += self.encodingDict[charText[i]]
		print(binaryString)
	
	def printDecodedString(self, encodedText):
		decodedString = ""
		currentIndex = 0
		while currentIndex < len(encodedText):
			letterFound = False
			currentNode = self.rootNode
			while not(letterFound) and currentIndex < len(encodedText):
				if currentNode.c != None:
					decodedString += currentNode.c
					currentIndex += 1
					letterFound = True
				else:
					if encodedText[currentIndex] == "0":
						#print("Moved Left")
						currentNode = currentNode.left
						currentIndex += 1
					elif encodedText[currentIndex] == "1":
						#print("Moved Right")
						currentNode = currentNode.right
						currentIndex += 1
		print(decodedString)

def main():
	hTree = HuffmanTree()
	charText = input()
	encodedText = input()
	hTree.buildData(charText)
	hTree.printEncodedString(charText)
	hTree.printDecodedString(encodedText)
	

main()