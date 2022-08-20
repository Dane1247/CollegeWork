#include <iostream>

//node class
class Node
{
private:
	int data;
	Node *leftNode, *rightNode;
public:
	Node(int uData = 0, Node *uLeftNode = 0, Node *uRightNode = 0);

	//getters
	int getData()const;
	Node* getLeftNode()const;
	Node* getRightNode()const;

	//setters
	void setLeftNode(Node *uLeftNode = 0);
	void setRightNode(Node *uRightNode = 0);
};

//default parameterized constructor
Node::Node(int uData, Node *uLeftNode, Node *uRightNode)
	:data(uData), leftNode(uLeftNode), rightNode(uRightNode)
{}

int Node::getData()const
{
	return data;
}

Node* Node::getLeftNode()const
{
	return leftNode;
}

Node* Node::getRightNode()const
{
	return rightNode;
}

void Node::setLeftNode(Node *uLeftNode)
{
	leftNode = uLeftNode;
}

void Node::setRightNode(Node *uRightNode)
{
	rightNode = uRightNode;
}

//binary Search Tree class
class BinarySearchTree
{
private:
	Node *topNode;
public:
	BinarySearchTree();
	void add(int uData);
	void print(Node *currentNode = 0);
};

BinarySearchTree::BinarySearchTree()
{
	topNode = 0;
}

//add method of the 
void BinarySearchTree::add(int uData)
{
	//creates the new node
	Node *newNode = new Node(uData);

	//if it is the first node in the tree, sets it to the topNode
	if (topNode == 0)
		topNode = newNode;
	else
	{
		//sets the node the new value will be compared to to the top node
		Node *tempNode = topNode;

		//while the newNode hasnt found its place in the tree, check the value of the newNode against the current node and move through the tree accordingly
		while (tempNode->getLeftNode() != newNode && tempNode->getRightNode() != newNode)
		{
			//checks if the value is greater or larger than the current node
			if (uData > tempNode->getData())
			{
				//checks if the right child is null if so sets the tempNode as the child of the appropriate node
				if (tempNode->getRightNode() == 0)
					tempNode->setRightNode(newNode);
				else
					tempNode = tempNode->getRightNode();
			}
			else
			{
				//checks if the right child is null if so sets the tempNode as the child of the appropriate node
				if (tempNode->getLeftNode() == 0)
					tempNode->setLeftNode(newNode);
				else
					tempNode = tempNode->getLeftNode();
			}
		}
	}
}

//inorder print method of the BinarySearchTree class
void BinarySearchTree::print(Node *currentNode)
{
	//if this was the first call of the funciton set the Node to topNode
	if (currentNode == 0)
		currentNode = topNode;

	//basic recursive traversial in LVR or inorder format
	if (currentNode->getLeftNode() != 0)
		print(currentNode->getLeftNode());

	std::cout << currentNode->getData() << " ";

	if (currentNode->getRightNode() != 0)
		print(currentNode->getRightNode());
}

int main()
{
	int uInput;

	BinarySearchTree bTree;

	std::cout << "Enter Values to Add to the Tree:(-999 to stop)" << std::endl;
	std::cin >> uInput;

	while (uInput != -999)
	{
		bTree.add(uInput);
		std::cin >> uInput;
	}

	std::cout << std::endl;

	std::cout << "Outputting Values in Inorder Format: " << std::endl;
	bTree.print();

	std::cout << std::endl;
}