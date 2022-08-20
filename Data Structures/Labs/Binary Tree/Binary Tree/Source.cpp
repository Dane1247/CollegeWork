#include <iostream>

//binary tree class
class arrayBinaryTree
{
private:
	static const int maxSize = 100;
	int data[100];
	int nodeCount;
public:
	arrayBinaryTree();
	void add(int uData);
	void preOrder(int initialNode);
};

//default constructor for arrayBinaryTree class
arrayBinaryTree::arrayBinaryTree()
{
	nodeCount = 0;
}

//adds node to the count position in the array, then increases the count
void arrayBinaryTree::add(int uData)
{
	data[nodeCount++] = uData;
}

//outputs all values in the tree in VLR pattern
void arrayBinaryTree::preOrder(int initialNode)
{
	std::cout << data[initialNode] << " ";

	if ((nodeCount - 1) >= ((2 * initialNode) + 1))
		preOrder((2 * initialNode) + 1);

	if ((nodeCount - 1) >= ((2 * initialNode) + 2))
		preOrder((2 * initialNode) + 2);
}

int main()
{
	int uInput;

	arrayBinaryTree bTree;

	std::cout << "Enter Values to Add to the Tree:(-999 to stop)" << std::endl;
	std::cin >> uInput;

	while (uInput != -999)
	{
		bTree.add(uInput);
		std::cin >> uInput;
	}

	std::cout << std::endl;

	std::cout << "Outputting Values in VLR Format: " << std::endl;
	bTree.preOrder(0);
}