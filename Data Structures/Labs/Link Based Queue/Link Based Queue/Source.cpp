#include <iostream>

//node class
class Node
{
private:
	int data;
	Node* nextNode;
public:
	Node(int uData, Node* uNextNode = 0);
	void setNextNode(Node* uNextNode = 0);
	Node* getNextNode();
	void setData(int uData);
	int getData();
};

//constructor with a default argument of nullpointer for the nextNode data member
Node::Node(int uData, Node* uNextNode)
{
	data = uData;
	nextNode = uNextNode;
}

//setter for the pointer of the node
void Node::setNextNode(Node* uNextNode)
{
	nextNode = uNextNode;
}

//getter for the nextNode data member
Node* Node::getNextNode()
{
	return nextNode;
}

//setter for data
void Node::setData(int uData)
{
	data = uData;
}

//getter for data 
int Node::getData()
{
	return data;
}

//link based queue class
class linkBasedQueue
{
private:
	Node *frontNode, *backNode;
public:
	linkBasedQueue();
	void enQueue(int uData);
	int deQueue();
	bool checkEmpty();
	void emptyQueue();
};

//constructor for linkBasedQueue class
linkBasedQueue::linkBasedQueue()
{
	frontNode = backNode = 0;
}

bool linkBasedQueue::checkEmpty()
{
	return frontNode == 0;
}

//adds a value to the queue
void linkBasedQueue::enQueue(int uData)
{
	//create new node
	Node *tempNode = new Node(uData);

	//if there are no nodes in the queue add it to the back and front
	if (backNode == 0)
	{
		frontNode = backNode = tempNode;
	}
	else
	{
		//sets the backNode link to the new node
		backNode->setNextNode(tempNode);

		//sets back equal to temp
		backNode = tempNode;
	}
}

int linkBasedQueue::deQueue()
{
	if (checkEmpty())
		return -999;

	//create a pointer to free up frontNode memory after the frontNode pointer has been moved
	Node *tempNode;

	//assighns the data value of the frontNode to a local var
	int returnValue = frontNode->getData();

	//assighns tempNode to the front node
	tempNode = frontNode;

	//moves the front node down the queue
	frontNode = frontNode->getNextNode();

	//returns memory from frontNode
	delete tempNode;

	//returns the data from the frontNode
	return returnValue;
}

//emptys the queue using the dequeue function
void linkBasedQueue::emptyQueue()
{
	std::cout << "Outputting all Values Using DeQueue Function: " << std::endl;

	while (!(checkEmpty()))
	{
		std::cout << this->deQueue() << " ";
	}

	std::cout << std::endl;
}

int main()
{
	//declares the linkBasedQueue
	linkBasedQueue intQueue;

	//declares int used to temporarly store user input
	int tempInt;
	
	//accepts user input
	std::cout << "Enter Values to Add to the Queue(-999 to stop): " << std::endl;
	std::cin >> tempInt;

	while (tempInt != -999)
	{
		intQueue.enQueue(tempInt);
		std::cin >> tempInt;
	}

	//outputs values from the queue using deQueue
	intQueue.emptyQueue();
}