#include <iostream>
#include <string>

class Node
{
private:
	int data;
	Node *nodeLink;
public:
	Node(int uData, Node* uNodeLink);
	int getData();
	void setNodeLink(Node* uNodeLink);
	Node* getNodeLink();
};

Node::Node(int uData, Node *uNodeLink = 0)
	:data(uData), nodeLink(uNodeLink)
{}

int Node::getData()
{
	return data;
}

Node* Node::getNodeLink()
{
	return nodeLink;
}

void Node::setNodeLink(Node* uNodeLink)
{
	nodeLink = uNodeLink;
}

class linkedStack
{
private:
	Node* topNode;
public:
	linkedStack();
	bool checkEmpty();
	void push(int uData);
	int pop();
	int peek();
	void printStack();
	Node* getTopNode();
};

linkedStack::linkedStack()
{
	topNode = 0;
}

Node* linkedStack::getTopNode()
{
	return topNode;
}

//returns true if empty
bool linkedStack::checkEmpty()
{
	return topNode == 0;
}

void linkedStack::push(int uData)
{
	//creates a temp pointer to the new node
	Node* tempNode = new Node(uData);

	//checks if empty and sets the new equal to the top if true
	if (checkEmpty())
	{
		topNode = tempNode;
	}
	else
	{
		//sets the nodeLink of the new node to the current topNode
		tempNode->setNodeLink(topNode);

		//sets the top to the new node
		topNode = tempNode;
	}
}

int linkedStack::pop()
{
	//returns error value if there are no nodes on the stack
	if (checkEmpty())
		return -999;

	//sets return value to the data value of the top node
	int returnValue = topNode->getData();

	//pointer to keep track of the top node
	Node* tempNode = topNode;

	//sets the top node to the next node in the stack
	topNode = topNode->getNodeLink();

	//delete current topnode
	delete tempNode;

	//returns data value of the previous top node
	return returnValue;
}

int linkedStack::peek()
{
	//if the stack is empty return -999 else return the data contained in the top node
	if (checkEmpty())
		return -999;
	else
		return topNode->getData();
}

void linkedStack::printStack()
{
	std::cout << "The Stack: " << std::endl;

	//keeps track of the number of elements outputed
	int stackCounter = 1;

	//outputs every value on the stack, incrimenting the counter to keep track of the current element after each output operation
	for (Node* tempNode = topNode; tempNode != 0; tempNode = tempNode->getNodeLink())
	{
		std::cout << "Element " << stackCounter << " is: " << tempNode->getData() << std::endl;
		stackCounter++;
	}
}

int main()
{
	linkedStack stackObject;

	//int used to read user input
	int uint;

	//sentinel value for the while loop
	std::string sValue = "Y";

	while (sValue == "Y" || sValue == "y")
	{
		std::cout << "Enter Interger to add to the stack: ";
		std::cin >> uint;
		stackObject.push(uint);
		
		std::cout << "Would you like to add another value to the stack?(Y/N): ";
		std::cin >> sValue;
	}

	std::cout << "outputing all data in the stack using the print function: " << std::endl;

	//prints out all current values on the stack
	stackObject.printStack();

	std::cout << std::endl;

	std::cout << "outputing all data in the stack using the pop function: " << std::endl;

	int stackCounter = 1, isEmptyFlag = 0, tempIntStorage = stackObject.pop();

	//clears the stack by outputing all of the data using the pop operation
	while (tempIntStorage != -999)
	{
		std::cout << "Element " << stackCounter << " is: " << tempIntStorage << std::endl;
		stackCounter++;
		tempIntStorage = stackObject.pop();
	}

	std::cout << "The Stack is Empty" << std::endl;
}