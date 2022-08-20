#include <iostream>
#include <string>

const int numArrayElements = 27;

//hash function that returns the hashed value of the key passed in
int hash(int uKeyValue);

//hash tabe class
class HashTable
{
private:
	//stores the key [0] and associated value [1]
	float hashTableArray[27];
public:
	HashTable();
	void add(int uKey);
	int lookUpValue(int uKey);
};

//default constructor for hashtable class
HashTable::HashTable()
{
	//sets all array elements to -999, used to check if the element has been filled or not
	for (int i = 0; i < 27; i++)
		hashTableArray[i] = -999;
}

//function to add a key to the table
void HashTable::add(int uKey)
{
	//hashes the key
	int hashValue = hash(uKey);

	//bool used to exit loop
	bool keyValueAdded = false;
	 
	//adds the value to the table using linear probing
	while (!keyValueAdded)
	{
		if (hashTableArray[hashValue] == -999)
		{
			hashTableArray[hashValue] = uKey;
			keyValueAdded = true;
		}
		else
			hashValue++;
	}
}

//function that looks up a key returns -1 if not in the table
int HashTable::lookUpValue(int uKey)
{
	//hashes the key
	int hashValue = hash(uKey);

	//checks until it finds the key or an empty element
	while (true)
	{
		if (hashTableArray[hashValue] == uKey)
			return hashTableArray[hashValue];
		else
			if (hashTableArray[hashValue] == -999)
				return -1;
			else
				hashValue++;
	}
}

int main()
{
	HashTable uHashTable;

	std::string sValue1 = "Y";
	int uInt1, uInt2, uInt3;

	//main UI loop
	while (sValue1 == "Y" || sValue1 == "y")
	{
		std::cout << "1) Add Value to the Hash Table\n2) Lookup Value in the Hash Table\nSelect Function: ";
		std::cin >> uInt1;

		std::cout << std::endl;

		if (uInt1 == 1)
		{
			std::cout << "Enter the Key to be Added: ";
			std::cin >> uInt2;

			uHashTable.add(uInt2);
		}
		else
			if (uInt1 == 2)
			{
				std::cout << "Enter the Key to be Looked Up: ";
				std::cin >> uInt2;

				uInt3 = uHashTable.lookUpValue(uInt2);

				if (uInt3 != -1)
					std::cout << "The Value is: " << uInt3 << std::endl;
				else
					std::cout << "The Entered Key is Not Present in the Hash Table" << std::endl;
			}
			else
				std::cout << "The Function Selection was Not Valid" << std::endl;

		std::cout << std::endl;

		std::cout << "Would you Like to Preform Another Operation(Y/N): ";
		std::cin >> sValue1;

		std::cout << std::endl;
	}
}

//hash function
int hash(int uKey)
{
	return uKey%numArrayElements;
}