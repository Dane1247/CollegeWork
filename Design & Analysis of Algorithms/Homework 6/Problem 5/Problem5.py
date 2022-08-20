def minimumStepCost(inputList, targetStep): 
	copyArray = [None]*targetStep
	if (targetStep == 0) or (targetStep == 1):
		return inputList[0]
	copyArray[0] = inputList[0]
	copyArray[1] = inputList[1]
	for i in range(2, targetStep):
		copyArray[i] = min(copyArray[i - 1], copyArray[i - 2]) + inputList[i]
	return min(copyArray[targetStep - 2], copyArray[targetStep - 1]) + inputList[len(inputList) - 1]
	
def main():
	numSteps = input()
	inputList = input().split(" ")
	for i in range(len(inputList)):
		inputList[i] = int(inputList[i])
	print(minimumStepCost(inputList, len(inputList)))

main()