#include <iostream>

void bubbleSort(int uArray[], int uArrayLength);

void swap(int &uVal1, int &uVal2);

int main()
{
	int arrayLength;

	//asks the user for data used to create an array
	std::cout << "Enter the desired length of the array: ";
	std::cin >> arrayLength;

	int *arrayPointer = new int [arrayLength];

	for (int i = 0; i < arrayLength; i++)
	{
		std::cout << "Enter value for element " << i + 1 << ": ";
		std::cin >> arrayPointer[i];
	}

	//sorts the array
	bubbleSort(arrayPointer, arrayLength);

	std::cout << std::endl << "Array Data Values: " << std::endl;

	for (int i = 0; i < arrayLength; i++)
	{
		std::cout << "Element " << i + 1 << " is: " << arrayPointer[i] << std::endl;
	}
}

void bubbleSort(int uArray[], int uArrayLength)
{
	bool arraySorted = false;

	for (int i = (uArrayLength - 1); i > 0; i--)
	{
		if (arraySorted)
			std::cout << "The Array is Sorted" << std::endl;
		else
		{
			arraySorted = true;
			for (int j = 0; j < i; j++)
				if (uArray[j] > uArray[j + 1])
				{
					swap(uArray[j], uArray[j + 1]);
					arraySorted = false;
				}
		}

	}
}

void swap(int &uVal1, int &uVal2)
{
	int temp = uVal1;
	uVal1 = uVal2;
	uVal2 = temp;
}