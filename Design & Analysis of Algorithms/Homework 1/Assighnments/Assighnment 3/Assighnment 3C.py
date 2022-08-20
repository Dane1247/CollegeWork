def partition(inputArray, lowValue, highValue): 
	i = (lowValue - 1)
	for j in range(lowValue , highValue):
		if ((int(inputArray[j][2]) < int(inputArray[highValue][2])) or ((int(inputArray[j][2]) == int(inputArray[highValue][2])) and (inputArray[j][0] < inputArray[highValue][0])) or \
		((int(inputArray[j][2]) == int(inputArray[highValue][2])) and (inputArray[j][0] == inputArray[highValue][0]) and (inputArray[j][1] < inputArray[highValue][1]))): 
			i = i + 1
			inputArray[i], inputArray[j] = inputArray[j], inputArray[i] 
	inputArray[i + 1], inputArray[highValue] = inputArray[highValue], inputArray[i + 1] 
	for x in range(len(inputArray)):
		for y in range(len(inputArray[x])):
			print(inputArray[x][y] + " ", end = '')
		print()
	print()
	return (i + 1)
  
def sort(inputArray, lowValue, highValue): 
	if lowValue < highValue: 
		partitionIndex = partition(inputArray,lowValue,highValue)
		sort(inputArray, lowValue, partitionIndex-1) 
		sort(inputArray, partitionIndex+1, highValue) 

def main():
	#numElements = int(input(""))
	#inputArray=  list()
	#for i in range(numElements):
	#	inputArray.append(input("").split(" "))
	inputArray = [['Emma', 'Watson', '2016'], ['Laura', 'Laham', '2018'], ['Mason', 'Park', '2017'], ['Nathan', 'Spaun', '2019'], ['Percy', 'Wesley', '2016'], ['Princess', 'Peach', '2017'], ['Simon', 'Marlow', '2018']]
	numNames = int(input(""))
	searchNamesList = list()
	for i in range(numNames):
		searchNamesList.append(input(""))

main()