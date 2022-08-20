def sort(inputArray):
	for i in range(len(inputArray)): 
		key = inputArray[i] 
		j = i-1
		while j >=0 and ((int(key[2]) < int(inputArray[j][2])) or ((int(key[2]) == int(inputArray[j][2])) and (key[0] < inputArray[j][0])) or \
		((int(key[2]) == int(inputArray[j][2])) and (key[0] == inputArray[j][0]) and (key[1] < inputArray[j][1]))):
				inputArray[j+1] = inputArray[j] 
				j -= 1
		inputArray[j+1] = key
		if i > 0:
			for x in range(len(inputArray)):
				for y in range(len(inputArray[x])):
					print(inputArray[x][y] + " ", end = '')
				print()
			print()
				
def main():
	#numElements = int(input(""))
	#inputArray=  list()
	#for i in range(numElements):
	#	inputArray.append(input("").split(" "))
	inputArray = [['danielle', 'rothermel', '2015'], ['sarah', 'shatan-pardo', '2017'], ['david', 'shatan-pardo', '2015'], ['alisa', 'nguyen', '2015'], ['todd', 'hirsch', '2017'], ['lina', 'kroehling', '2015'], ['jess', 'geiger', '2014'], ['anita', 'garcia', '2017']]
	sort(inputArray)

main()