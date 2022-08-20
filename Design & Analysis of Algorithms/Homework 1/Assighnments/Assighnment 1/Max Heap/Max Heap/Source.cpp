#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include "limits.h"

using namespace std;

void heapify(vector<int> &maxHeap, int currentIndex);

bool verify(vector<int> &maxHeap, int currentIndex);

class MaxHeap {
private:
	vector<int> data;
public:
MaxHeap()
{}

int size()
{
	std::cout << data.size() << std::endl;
	return data.size();
}

int maxLookup()
{
	std::cout << data[0] << std::endl;
	return data[0];
}

void extractMax()
{
	data.erase(data.begin());
	while(!verify(data, data.size()-1))
		heapify(data, data.size() - 1);
}

void insert(int userData)
{
	data.insert(data.begin(), userData);
	while (!verify(data, data.size() - 1))
		heapify(data, data.size() - 1);
}

void remove(int index)
{
	data.erase(data.begin() + index);
	while (!verify(data, data.size() - 1))
		heapify(data, data.size() - 1);
}

void print()
{
	for (int i = 0; i < data.size(); i++)
		std::cout << data[i] << "  | ";
}
};

int main() {
	MaxHeap* mainHeap = new MaxHeap();

	int numIterations;
	cin >> numIterations;

	std::string userInput;
	int userInputInt;
	for (int i = 0; i < numIterations; i++)
	{
		std::cin >> userInput;
		if (userInput == "size")
		{
			mainHeap->size();
		}
		else
			if (userInput == "maxLookup")
			{
				mainHeap->maxLookup();
			}
			else
				if (userInput == "extractMax")
				{
					mainHeap->extractMax();
				}
				else
					if (userInput == "insert")
					{
						cin >> userInputInt;
						mainHeap->insert(userInputInt);
					}
					else
						if (userInput == "delete")
						{
							cin >> userInputInt;
							mainHeap->remove(userInputInt);
						}
						else
							if (userInput == "print")
							{
								mainHeap->print();
							}
	}
}


void heapify(vector<int> &maxHeap, int currentIndex)
{
	if (currentIndex > 0)
	{
		int parentNode = (currentIndex - 1) / 2;
		if (maxHeap[currentIndex] > maxHeap[parentNode])
		{
			int tempVar = maxHeap[currentIndex];
			maxHeap[currentIndex] = maxHeap[parentNode];
			maxHeap[parentNode] = tempVar;
		}
		else
			heapify(maxHeap, currentIndex - 1);
	}
	else
		return;
}

bool verify(vector<int> &maxHeap, int currentIndex)
{
	if (currentIndex > 0)
	{
		int parentNode = (currentIndex - 1) / 2;
		if (maxHeap[currentIndex] > maxHeap[parentNode])
			return false;
		else
		{
			verify(maxHeap, currentIndex - 1);
		}
	}
	else
		return true;
}