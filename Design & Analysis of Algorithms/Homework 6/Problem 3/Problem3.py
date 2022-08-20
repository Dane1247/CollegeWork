def lillyPadRecursive(lillyPadList, souceIndex, targetIndex): 
    if (targetIndex == souceIndex): 
        return 0
    if (lillyPadList[souceIndex] == 0): 
        return float('inf') 
    minJumps = float('inf') 
    for i in range(souceIndex + 1, targetIndex + 1): 
        if (i < souceIndex + lillyPadList[souceIndex] + 1): 
            tempJumps = lillyPadRecursive(lillyPadList, i, targetIndex) 
            if (tempJumps != float('inf') and 
                       tempJumps + 1 < minJumps): 
                minJumps = tempJumps + 1
    return minJumps

def main():
	numLillyPads = int(input())
	lillyPadList = input().split(" ")
	for i in range(len(lillyPadList)):
		lillyPadList[i] = int(lillyPadList[i])
	minJumpsVal = lillyPadRecursive(lillyPadList, 0, len(lillyPadList))
	if (minJumpsVal != float('inf')):
		print(minJumpsVal)
	else:
		print("-1")

main()