def radixSort(inputArray): 
	maxValue = max(inputArray) 
	exponent = 1
	while sorted(inputArray) != inputArray: 
		subCountingSort(inputArray,exponent) 
		printArray(inputArray)
		exponent *= 10

def subCountingSort(inputArray, currentExponent): 
	arrayLen = len(inputArray) 
	returnArray = [0] * (arrayLen) 
	countArray = [0] * (10) 
	for i in range(arrayLen): 
		countArray[int((inputArray[i] / currentExponent) % 10)] += 1
	for i in range(1,10): 
		countArray[i] += countArray[i - 1] 
	i = arrayLen - 1
	while i >= 0: 
		returnArray[int(countArray[int(inputArray[i]/currentExponent) % 10] - 1)] = inputArray[i] 
		countArray[int((inputArray[i]/currentExponent) % 10)] -= 1
		i -= 1
	i = 0
	for i in range(0, len(inputArray)): 
		inputArray[i] = returnArray[i] 
		
def printArray(inputArray):
	for i in range(len(inputArray)):
		if i < (len(inputArray) - 1):
			print(str(inputArray[i]) + " ", end = '')
		else:
			print(str(inputArray[i]) + " ")
		
def main():
	#numChars = int(input())
	#inputList = input().split(" ")
	#for i in range(len(inputList)):
	#	inputList[i] = int(inputList[i])
	numChars = 12
	inputList = [9, 87, 199, 15, 3, 214, 19, 26, 58, 2, 102, 23]
	for i in range(len(inputList)):
		inputList[i] = int(inputList[i])
	radixSort(inputList)

main()