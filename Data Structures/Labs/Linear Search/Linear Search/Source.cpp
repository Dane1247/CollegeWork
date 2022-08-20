#include <iostream>

int searchArray(const int &sNum, const int &arraySize, int uArray[]);

int main()
{
	int arraySize;
	int uValue;

	std::cout << "Enter size of a desired array: ";
	std::cin >> arraySize;

	int *arrayPointer = new int[arraySize];

	for (int i = 0; i < arraySize; i++)
	{
		std::cout << "Enter Element " << i + i << " of the array: ";
		std::cin >> arrayPointer[i];
	}

	std::cout << std::endl;

	for (int i = 0; i < arraySize; i++)
	{
		std::cout << arrayPointer[i] << " ";
	}

	std::cout << std::endl;

	std::cout << "what value would you like to search for?: ";
	std::cin >> uValue;

	std::cout << "Return Value of SearchArray function: " << searchArray(uValue, arraySize, arrayPointer) << std::endl;
}

//searches for the value based on arguments
int searchArray(const int &sNum, const int &arraySize, int uArray[])
{
	for (int i = 0; i < arraySize; i++)
	{
		if (sNum == uArray[i])
			return i;
	}
	return -1;
}