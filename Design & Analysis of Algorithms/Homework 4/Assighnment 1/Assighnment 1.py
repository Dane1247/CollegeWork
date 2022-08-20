class Node:
	def __init__(self, nodeLetter = "", isLeaf = False):
		self.isLeaf = isLeaf
		self.nodeLetter = nodeLetter
		self.childNodes = list()
	
	def addChild(self, nodeLetter = "", isLeaf = False):
		newNode = Node(nodeLetter, isLeaf)
		self.childNodes.append(newNode)
		return newNode
		
class TryClass:
	def __init__(self):
		self.rootNode = Node("Root", False)
		
	def  lookupStart(self, searchKey):
		valuePrinted = [False]
		for i in range(len(self.rootNode.childNodes)):
			if self.rootNode.childNodes[i].nodeLetter == searchKey[0]:
				self.lookupRecursive(self.rootNode.childNodes[i], searchKey, 1, valuePrinted)
		if not(valuePrinted[0]):
				print("0")
				valuePrinted[0] = True

	def lookupRecursive(self, currentNode, searchKey, letterNum, valuePrinted):
		if ((letterNum == len(searchKey)) and (currentNode.isLeaf)):
			if not(valuePrinted[0]):
				print("1")
				valuePrinted[0] = True
		elif ((letterNum == len(searchKey)) and (currentNode.isLeaf)):
			if not(valuePrinted[0]):
				print("0")
				valuePrinted[0] = True
		elif letterNum < len(searchKey):
			for i in range(len(currentNode.childNodes)):
				if currentNode.childNodes[i].nodeLetter == searchKey[letterNum]:
					self.lookupRecursive(currentNode.childNodes[i], searchKey, letterNum + 1, valuePrinted)
			if not(valuePrinted[0]):
				print("0")
				valuePrinted[0] = True

	def  insertStart(self, insertKey):
		nodeFound = False
		for i in range(len(self.rootNode.childNodes)):
			if self.rootNode.childNodes[i].nodeLetter == insertKey[0] and not(nodeFound):
				self.insertRecursive(self.rootNode.childNodes[i], insertKey, 1)
				nodeFound = True
		if nodeFound == False:
			newChild = self.rootNode.addChild(insertKey[0], False)
			self.insertRecursive(newChild, insertKey, 1)

	def insertRecursive(self, currentNode, insertKey, letterNum):
		if (letterNum == (len(insertKey))):
			currentNode.isLeaf = True
			return True
		elif (letterNum < (len(insertKey))):
			nodeFound = False
			for i in range(len(currentNode.childNodes)):
				if currentNode.childNodes[i].nodeLetter == insertKey[letterNum]:
					self.insertRecursive(currentNode.childNodes[i], insertKey, letterNum + 1)
					nodeFound = True
			if nodeFound == False:
				newChild = currentNode.addChild(insertKey[letterNum], False)
				self.insertRecursive(newChild, insertKey, letterNum + 1)
				
	def info(self, numNodeLeafsArray, currentNode):
		for i in range(len(currentNode.childNodes)):
			self.info(numNodeLeafsArray, currentNode.childNodes[i])
		numNodeLeafsArray[0] += 1
		if currentNode.isLeaf:
			numNodeLeafsArray[1] += 1
		
	def  removeStart(self, removeKey):
		firstBranch = [False]
		for i in range(len(self.rootNode.childNodes)):
			if self.rootNode.childNodes[i].nodeLetter == removeKey[0]:
				self.removeRecursive(self.rootNode.childNodes[i], removeKey, 1, firstBranch)

	def removeRecursive(self, currentNode, removeKey, letterNum, firstBranch):
		if (letterNum < len(removeKey)):
			for i in range(len(currentNode.childNodes)):
					if currentNode.childNodes[i].nodeLetter == removeKey[letterNum]:
						self.removeRecursive(currentNode.childNodes[i], removeKey, letterNum + 1, firstBranch)
		if (letterNum < len(removeKey)) and not(firstBranch[0]) and (len(currentNode.childNodes) > 1):
			for i in range(len(currentNode.childNodes)):
				if firstBranch[0] == False:
					if currentNode.childNodes[i].nodeLetter == removeKey[letterNum]:
						currentNode.childNodes.pop(i)
						firstBranch[0] = True
		elif not(firstBranch[0]) and len(currentNode.childNodes) == 1:
			currentNode.childNodes = []
		
	def alphabetical(self, completeWordsArray):
		self.alphabeticalRecursive(completeWordsArray, self.rootNode)
		return completeWordsArray.sort()
		
	def alphabeticalRecursive(self, wordsArray, currentNode, currentPathWord = ""):
		if currentNode.nodeLetter != "Root":
			currentNodePath = currentPathWord + currentNode.nodeLetter
			if currentNode.isLeaf:
				wordsArray.append(currentNodePath)
		else:
			currentNodePath = ""
		for i in range(len(currentNode.childNodes)):
				self.alphabeticalRecursive(wordsArray, currentNode.childNodes[i], currentNodePath)
		
	def autocomplete(self, prefix, numExtraCharacters):
		returnNode = []
		self.autocompleteRecusrive(self.rootNode, prefix, returnNode)
		initialWordList = []
		self.alphabeticalRecursive(initialWordList, returnNode[0], prefix[0:len(prefix) - 1])
		maxNumChars = len(prefix) + numExtraCharacters
		finalWordList = []
		for i in range(len(initialWordList)):
			if len(initialWordList[i]) <= maxNumChars or numExtraCharacters == -1:
				finalWordList.append(initialWordList[i])
		finalWordList.sort()
		for i in range(len(finalWordList)):
			print(finalWordList[i] + " ", end = '')
		print()

	def autocompleteRecusrive(self, currentNode, searchPrefix, returnNode, currentPathWord = ""):
		if currentNode.nodeLetter != "Root":
			currentNodePath = currentPathWord + currentNode.nodeLetter
			if currentNodePath == str(searchPrefix):
				returnNode.append(currentNode)
				return
		else:
			currentNodePath = ""
		for i in range(len(currentNode.childNodes)):
				self.autocompleteRecusrive(currentNode.childNodes[i], searchPrefix, returnNode, currentNodePath)
		
def main():
	numInput = int(input(""))
	trieTree = TryClass()
	for i in range(numInput):
		userInput = input("").split(" ")
		if userInput[0] == "insert":
			trieTree.insertStart(userInput[1])
		elif userInput[0] == "remove":
			trieTree.removeStart(userInput[1])
		elif userInput[0] == "lookup":
			trieTree.lookupStart(str(userInput[1]))
		elif userInput[0] == "alphabetical":
			completeWordsArray = []
			trieTree.alphabetical(completeWordsArray)
			completeWordsArray.sort()
			for i in range(len(completeWordsArray)):
				print(completeWordsArray[i])
		elif userInput[0] == "info":
			infoArray = [0, 0]
			trieTree.info(infoArray, trieTree.rootNode)
			print(str(infoArray[0]) + " "+ str(infoArray[1]))
		elif userInput[0] == "autocomplete":
			trieTree.autocomplete(userInput[1], int(userInput[2]))
			

main()
		