#include <iostream>

//singly linked node class
class Node
{
private:
	int data;
	Node *nextNode;
public:
	Node(int uData, Node *uNextNode = 0);
	Node* getNextNode();
	void setNextNode(Node *uNextNode);
	int getData();
};

//Constructor for Node class
Node::Node(int uData, Node *uNextNode)
{
	data = uData;
	nextNode = uNextNode;
}

//getter for 'data' data member
int Node::getData()
{
	return data;
}

//getter for nextNode data member
Node* Node::getNextNode()
{
	return nextNode;
}

//setter for nextNode data member
void Node::setNextNode(Node *uNextNode)
{
	nextNode = uNextNode;
}

class singlyLinkedSortedList
{
private:
	Node *topNode;
public:
	singlyLinkedSortedList();
	void add(int uData);
	bool checkEmpty();
	void printList();
};

//default constructor for singlyLinkedSortedList class
singlyLinkedSortedList::singlyLinkedSortedList()
{
	topNode = 0;
}

//returns true if empty
bool singlyLinkedSortedList::checkEmpty()
{
	return topNode == 0;
}

//function used to add to the list
void singlyLinkedSortedList::add(int uData)
{
	//creates new node
	Node *newNode = new Node(uData);

	//if the list is empty, set the topNode equal to tempNode
	if (checkEmpty())
		topNode = newNode;
	else
	{
		//creates a pointer to travel though the list and test data values
		Node *tempNodeBack = topNode;

		//creates pointer to travel through the list one node before tempNodeBack
		Node *tempNodeFront = topNode;

		//delays the tempNodeFront from moving back one node by a single operation
		bool binaryCounter = false;

		//moves through the list until it finds the correct place for the new node
		if (uData > tempNodeBack->getData())
		{
			while (tempNodeBack != 0 && uData > tempNodeBack->getData())
			{
				if (!binaryCounter)
					binaryCounter = true;
				else
					if (binaryCounter)
						tempNodeFront = tempNodeFront->getNextNode();

				tempNodeBack = tempNodeBack->getNextNode();
			}

			//sets the nextNode member of the correct node in the list to the newNode
			tempNodeFront->setNextNode(newNode);

			//sets the nextNode member of the new node in the list to the correct node
			newNode->setNextNode(tempNodeBack);
		}
		else
		{
			//if it is the smallest value add it to the front of the list
			newNode->setNextNode(topNode);
			topNode = newNode;
		}
		
	}
}

//prints the list
void singlyLinkedSortedList::printList()
{
	std::cout << "The Current List: " << std::endl;

	for (Node *tempNode = topNode; tempNode != 0; tempNode = tempNode->getNextNode())
	{
		std::cout << tempNode->getData() << " ";
	}

	std::cout << std::endl;
}

int main()
{
	singlyLinkedSortedList sortedList;

	int tempInt = 0;

	//accepts user input and displays the list after each addition
	std::cout << "Enter Value to Add to the List: ";
	std::cin >> tempInt;

	while (tempInt != -999)
	{
		sortedList.add(tempInt);
		sortedList.printList();

		std::cout << "Enter Value to Add to the List: ";
		std::cin >> tempInt;
	}
}