#include <iostream>

class arrayQueue
{
private:
	static const int maxSize = 10;
	int queue[maxSize];
	int front, back, count;
public:
	arrayQueue();
	bool enqueue(int uData);
	int dequeue();
	bool isEmpty();
};

arrayQueue::arrayQueue()
{
	front = back = count = 0;
}

bool arrayQueue::enqueue(int uData)
{
	if (count++ == maxSize)
	{
		count--;
		std::cout << "The queue has reached maximum capacity" << std::endl;
		return false;
	}
	else
	{
		queue[back++] = uData;
		if (back >= maxSize)
			back = 0;

	}
}

int arrayQueue::dequeue()
{
	if (isEmpty())
		return -999;

	count--;
	int returnValue = queue[front++];

	if (front > maxSize)
		front = 0;

	return returnValue;
}

bool arrayQueue::isEmpty()
{
	return count == 0;
}

int main()
{
	arrayQueue arrayQueue1;

	int uValue1, uValue2;
	std::cout << "How many values would you like to enter into the queue: ";
	std::cin >> uValue1;

	for (int i = 0; i < uValue1; i++)
	{
		std::cout << "Enter value " << i + 1 << ": ";
		std::cin >> uValue2;
		arrayQueue1.enqueue(uValue2);
	}

	std::cout << "Outputting all data in the queue: " << std::endl;

	for (int i = 0; i < uValue1; i++)
	{
		std::cout << arrayQueue1.dequeue() << " ";
	}
	
	std::cout << std::endl;
}