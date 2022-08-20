#include <iostream>

class arrayStack
{
private:
	static const int maxSize = 10;
	int intArray[maxSize];
	int top;
public:
	arrayStack();
	bool push(int uData);
	int pop();
	bool isEmpty();
};

arrayStack::arrayStack()
{
	top = 0;
}

bool arrayStack::push(int uData)
{
	//check if the stack is full
	if (top + 1 >= maxSize)
		return false;

	//assighns the data to the top of the stack and moves the top up
	intArray[top++] = uData;
}

int arrayStack::pop()
{
	//checks if the stack is empty
	if (isEmpty())
		return -999;
	
	return intArray[--top];
}

bool arrayStack::isEmpty()
{
	return top == 0;
}

int main()
{
	arrayStack stackObject;

	int uNum1, uNum2;
	std::cout << "How many intergers would you like to push onto the stack?(Max 10): ";
	std::cin >> uNum1;

	for (int i = 0; i < uNum1; i++)
	{
		std::cout << "Enter int: ";
		std::cin >> uNum2;
		stackObject.push(uNum2);
	}
	
	std::cout << "Outputing values on the stack: " << std::endl;

	do
	{
		std::cout << stackObject.pop() << " ";
	} while (!(stackObject.isEmpty()));
}