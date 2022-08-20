def sequenceGenStart(requiredSum, coinValueList):
	numPossibleSequences = [0]
	coinNumList = list()
	for i in range(len(coinValueList)):
		coinNumList.append(0)
	sequenceGenRecursive(requiredSum, requiredSum, coinNumList, coinValueList, 0, numPossibleSequences)
	print(numPossibleSequences[0])

def sequenceGenRecursive(requiredSum, parentRemainder, coinNumList, coinValueList, currentCoin, possibleNumSequences):
	localCoinNumList = list()
	for i in range(len(coinNumList)):
		localCoinNumList.append(coinNumList[i])
	if (currentCoin < len(coinValueList)):
		for i in range((parentRemainder//coinValueList[currentCoin]) + 1):
			localCoinNumList[currentCoin] =  i
			sequenceGenRecursive(requiredSum, parentRemainder - coinValueList[currentCoin]*i, localCoinNumList, coinValueList, currentCoin + 1, possibleNumSequences)
	elif (currentCoin == len(coinValueList)):
		currentTotal = 0
		for i in range(len(coinNumList)):
			currentTotal += coinNumList[i] * coinValueList[i]
		if currentTotal == requiredSum:
			possibleNumSequences[0] += 1

def main():
	requiredSum = int(input())
	numCoinSum = int(input())
	coinValueList = input().split(" ")
	for i in range(len(coinValueList)):
		coinValueList[i] = int(coinValueList[i])
	coinValueList = sorted(coinValueList, reverse = True)
	sequenceGenStart(requiredSum, coinValueList)
		

main()