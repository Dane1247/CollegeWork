#include <iostream>
#include <string>
#include <vector>

//returns false if the string contains digits
bool checkString(const std::string &testString);

int main()
{
	std::vector<std::string> stringArray;
	std::string tempString;
	
	std::cout << "Enter Sentence: " << std::endl;

	//accepts user input
	do
	{
		std::cin >> tempString;
		stringArray.push_back(tempString);
	}
	while (tempString != "=");

	//outputs and checks if string is a character
	for (std::vector<std::string>::const_iterator stringIterator = stringArray.cbegin(); stringIterator != stringArray.cend(); stringIterator++)
	{
		if (!(checkString(*stringIterator)))
		{
			//if so converts the string to a float and multiplies it by 2
			std::cout << 2 * std::stof(*stringIterator) << std::endl;
		}
		else
			std::cout << *stringIterator << std::endl;
	}
}

bool checkString(const std::string &testString)
{
	return testString.find_first_of("0123456789") == std::string::npos;
}