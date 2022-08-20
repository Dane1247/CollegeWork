#include <iostream>

const int maxSize = 100;

//swaps the values of the two arguments
void swapValues(int &uVal1, int &uVal2);

//minheap class
class minHeap
{
private:
	int heapArray[maxSize];
	int numNodes;
public:
	minHeap();
	void add(int uData);
	int deleteElement();
	void preOrder(int uNodePointer = 1);
};

//default constructor for minHeap class
minHeap::minHeap()
	:numNodes(0)
{
	heapArray[0] = 0;
}

//adds a value to the minHeap
void minHeap::add(int uData)
{
	//inserts the new value into the tree
	//element 0 is never used
	heapArray[++numNodes] = uData;

	//creates a temp pointer to the most recently inserted element
	int tempNodePointer = numNodes;

	//checks if there is more than 1 node, if so swaps values accordingly
	if (numNodes > 1)
		while ((heapArray[tempNodePointer/2] > heapArray[tempNodePointer]) && tempNodePointer != 1)
		{
			//if the current node is smaller than its parent and its not the root, 
			//swap and set the pointer to the new location of the new node
			swapValues(heapArray[tempNodePointer], heapArray[tempNodePointer / 2]);
			tempNodePointer = tempNodePointer / 2;
		}
}

//removes and element from the minHeap
int minHeap::deleteElement()
{
	//declares the interger that is going to be returned
	int returnInt;

	//checks if there are any nodes in the tree
	if (numNodes > 0)
	{
		//sets the return value to the root of the tree
		returnInt = heapArray[1];

		//sets the root to the last element added, and post-decriments the numNodes var
		heapArray[1] = heapArray[numNodes--];

		//checks if there is more than 1 node, if so swaps values where appropriate
		if (numNodes > 1)
		{
			//sets a pointer to the root to keep track of the location of the moved node
			int tempNodePointer = 1;

			//while the value of the newNode is greater than one of its children, and it exists, swaps with the smaller of those children
			while (((2 * tempNodePointer) <= numNodes) && (heapArray[tempNodePointer] > heapArray[(2 * tempNodePointer)]) || (((2 * tempNodePointer) + 1) <= numNodes) && (heapArray[tempNodePointer] > heapArray[(2 * tempNodePointer) + 1]))
			{
				//checks if there are 2 children
				if (((2 * tempNodePointer) <= numNodes) && ((2 * tempNodePointer) + 1 <= numNodes))
				{
					//if so checks which child is larger
					if (heapArray[(2 * tempNodePointer)] < heapArray[(2 * tempNodePointer) + 1])
					{
						swapValues(heapArray[tempNodePointer], heapArray[(2 * tempNodePointer)]);
						tempNodePointer = 2 * tempNodePointer;
					}
					else
					{
						if (heapArray[(2 * tempNodePointer)] > heapArray[(2 * tempNodePointer) + 1])
						{
							swapValues(heapArray[tempNodePointer], heapArray[(2 * tempNodePointer) + 1]);
							tempNodePointer = (2 * tempNodePointer) + 1;
						}
						else
						{
							//if the two children are of equal value, default to left child if it exists
							swapValues(heapArray[tempNodePointer], heapArray[(2 * tempNodePointer) + 1]);
							tempNodePointer = (2 * tempNodePointer) + 1;
						}
					}
				}
				else
				{
					// if only a single child exists, swap with the existent one
					if ((2 * tempNodePointer) <= numNodes)
					{
						swapValues(heapArray[tempNodePointer], heapArray[(2 * tempNodePointer)]);
						tempNodePointer = 2 * tempNodePointer;
					}
					else
						if ((2 * tempNodePointer) + 1 <= numNodes)
						{
							swapValues(heapArray[tempNodePointer], heapArray[(2 * tempNodePointer) + 1]);
							tempNodePointer = (2 * tempNodePointer) + 1;
						}
				}
			}
		}
	}
	else
	{
		//if there are no nodes in the tree, return error value
		returnInt = -999;
	}

	//returns the old root value
	return returnInt;
}

//outputs values contained within the tree in preorder format
void minHeap::preOrder(int uNodePointer)
{
	std::cout << heapArray[uNodePointer] << " ";

	if ((2 * uNodePointer) <= numNodes)
		preOrder(uNodePointer * 2);

	if (((2 * uNodePointer) + 1) <= numNodes)
		preOrder((uNodePointer * 2) + 1);
}

int main()
{
	//declares the minHeap class object
	minHeap uMinHeap;

	//declares ints used to intput and output from the tree 
	int uInt, outputInt;

	//accepts user input to fill the tree
	std::cout << "Enter values to add to the minHeap(-999 to stop):" << std::endl;
	std::cin >> uInt;

	while (uInt != -999)
	{
		uMinHeap.add(uInt);
		std::cin >> uInt;
	}

	std::cout << std::endl;

	//outputs from the tree using the delete function
	std::cout << "Outputting all values using the delete function of the minHeap class:" << std::endl;

	outputInt = uMinHeap.deleteElement();
	while (outputInt != -999)
	{
		std::cout << outputInt << " ";
		outputInt = uMinHeap.deleteElement();
	}

	std::cout << std::endl;
}

//swaps the values of the two arguments
void swapValues(int &uVal1, int &uVal2)
{
	int tempInt = uVal2;
	uVal2 = uVal1;
	uVal1 = tempInt;
}