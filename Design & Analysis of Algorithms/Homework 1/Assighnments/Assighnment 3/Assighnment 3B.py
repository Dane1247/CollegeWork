def sort(inputArray): 
	if len(inputArray) >1: 
		arrayMidpoint = len(inputArray)//2
		leftSide = inputArray[:arrayMidpoint]
		rightSide = inputArray[arrayMidpoint:]
		sort(leftSide)
		sort(rightSide)
		i = j = k = 0
		while i < len(leftSide) and j < len(rightSide): 
			if ((int(leftSide[i][2]) < int(rightSide[j][2])) or ((int(leftSide[i][2]) == int(rightSide[j][2])) and (leftSide[i][0] < rightSide[j][0])) or \
			((int(leftSide[i][2]) == int(rightSide[j][2])) and (leftSide[i][0] == rightSide[j][0]) and (leftSide[i][1] < rightSide[j][1]))):
				inputArray[k] = leftSide[i] 
				i+=1
			else: 
				inputArray[k] = rightSide[j] 
				j+=1
			k+=1
		while i < len(leftSide): 
			inputArray[k] = leftSide[i] 
			i+=1
			k+=1
		while j < len(rightSide): 
			inputArray[k] = rightSide[j] 
			j+=1
			k+=1
				
def main():
	#numElements = int(input(""))
	#inputArray=  list()
	#for i in range(numElements):
	#	inputArray.append(input("").split(" "))
	inputArray = [['danielle', 'rothermel', '2015'], ['sarah', 'shatan-pardo', '2017'], ['david', 'shatan-pardo', '2015'], ['alisa', 'nguyen', '2015'], ['todd', 'hirsch', '2017'], ['lina', 'kroehling', '2015'], ['jess', 'geiger', '2014'], ['anita', 'garcia', '2017']]
	sort(inputArray)
	for x in range(len(inputArray)):
		for y in range(len(inputArray[x])):
			print(inputArray[x][y] + " ", end = '')
		print()
	print()

main()