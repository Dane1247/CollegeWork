#include <iostream>
#include <fstream>
#include <string>
#include <cmath>

//an interpriter for a basic BORG language, follows the following rules
//a sample text file is included, need to change filepath in main to the filepath you will be using
/*
Program Specification :

Build a hash table using chaining as the collision resolution technique.Insertions into the hash table will correspond to declarations of variables and values in a program, searches will be requests for the value of a variable.Some variables will be local and have a narrow scope while some variables will be global.

The program will take input from a file, another program written in the omnipotent programming language BORG(Bionicly Omnipotent Resistance Grinders) and generate output from this program.

The BORG language has the following commands(keywords) :

	START - FINISH blocks.Indicating different scopes.
	COM - Single line comments : Text should be ignored if on the same line
	VAR varName – Variable Declaration, adds “varName” to the hash table.
	variable = expression – Assignment statements, ie GEORGE = 122. Find GEORGE in the hash table and assign 122 to it.
	++ - increment operator, syntax : VARIABLE++
	-- - decrement operator, syntax : VARIABLE --
	expressions, expressions are limited to unary and binary arithmetic, or variable names
	supported operators : +-/ *% ^ (plus, minus, divide, multiple, modulo, exponent)
	PRINT – syntax PRINT expression.If the expression is a variable, and this variable is not in scope, then an error message indicating unknown variable x at line number y.The value printed if there is a variable in scope should be the variable with the closest scope.
	Errors – other than the print statements, our interpreter will not be responsible for detecting errors, syntax errors should be disregarded if encountered, assume that the source file is correct.

	Our hash function : sum the ordinal values of the characters of the variable multiplied by their position in the string(1 - indexing), then taking the modulo by TABLESIZE.

	ie.The variable ABC = (65 * 1 + 66 * 2 + 67 * 3) % TABLESIZE

	All tokens are separated by one space or a new line.

	Output : for this assignment, run your interpreter on this sample source program as well as a program of your own, and turn it the output from both, as well as the source code from your BORG program as well as source code of the assignment and its executable.Zip is good.
*/
//hashTableSize
const int numArrayElements = 100;

//largest number of scopes able to be opened within eachother at any given time
const int maxNumScopeInstances = 10;

//hash function that returns the hashed value of the key passed in
int hash(std::string uVarName);

//linked list node class
class linkedListNode
{
private:
	std::string varName;
	float varValue;
	int scopeLevel;
	int scopeLevelInstances[maxNumScopeInstances];
	linkedListNode *nodeLink;
public:
	linkedListNode(std::string uVarName, float uVarValue, int uScopeLevel, int uScopeLevelInstance[], linkedListNode *uNodeLink = 0);
	int getScopeLevel();
	int getScopeLevelInstance(int uArrayElement);
	float getVarValue();
	std::string getVarName();
	void setScopeLevel(int uScopeLevel);
	void setVarValue(float uVarValue);
	void setNodeLink(linkedListNode* uNodeLink);
	linkedListNode* getNodeLink();
};

//default constructor for linkedListNode
linkedListNode::linkedListNode(std::string uVarName, float uVarValue, int uScopeLevel, int uScopeLevelInstance[], linkedListNode *uNodeLink)
	:varValue(uVarValue), varName(uVarName), scopeLevel(uScopeLevel), nodeLink(uNodeLink)
{
	for (int i = 0; i < maxNumScopeInstances; i++)
		scopeLevelInstances[i] = uScopeLevelInstance[i];
}

//getter for var value
float linkedListNode::getVarValue()
{
	return varValue;
}

//getter for var name
std::string linkedListNode::getVarName()
{
	return varName;
}

//getter for scopeLevel
int linkedListNode::getScopeLevel()
{
	return scopeLevel;
}

//getter for scopeLevelInstance
int linkedListNode::getScopeLevelInstance(int uArrayElement)
{
	return scopeLevelInstances[uArrayElement];
}

//setter for scopeLevel
void linkedListNode::setScopeLevel(int uScopeLevel)
{
	scopeLevel = uScopeLevel;
}

//setter for varValue
void linkedListNode::setVarValue(float uVarValue)
{
	varValue = uVarValue;
}

//getter for nodeLink
linkedListNode* linkedListNode::getNodeLink()
{
	return nodeLink;
}

//setter for nodeLink
void linkedListNode::setNodeLink(linkedListNode* uNodeLink)
{
	nodeLink = uNodeLink;
}

//node class template
template <class T>
class stackNode
{
private:
	T data;
	stackNode *nodeLink;
public:
	stackNode(T uData, stackNode* uNodeLink = 0);
	T getData();
	void setNodeLink(stackNode* uNodeLink);
	stackNode<T>* getNodeLink();
};

template <class T>
stackNode<T>::stackNode(T uData, stackNode *uNodeLink)
	:data(uData), nodeLink(uNodeLink)
{}

template <class T>
T stackNode<T>::getData()
{
	return data;
}

template <class T>
stackNode<T>* stackNode<T>::getNodeLink()
{
	return nodeLink;
}

template <class T>
void stackNode<T>::setNodeLink(stackNode* uNodeLink)
{
	nodeLink = uNodeLink;
}

//float linked stack class
class linkedFloatStack
{
private:
	stackNode<float>* topNode;
	int nodeCount;
public:
	linkedFloatStack();
	bool checkEmpty();
	void push(float uData);
	float pop();
	float peek();
	stackNode<float> *getTopNode();
	int getNodeCount();
};

linkedFloatStack::linkedFloatStack()
{
	topNode = 0;
	nodeCount = 0;
}

stackNode<float>* linkedFloatStack::getTopNode()
{
	return topNode;
}

int linkedFloatStack::getNodeCount()
{
	return nodeCount;
}

//returns true if empty
bool linkedFloatStack::checkEmpty()
{
	return topNode == 0;
}

void linkedFloatStack::push(float uData)
{
	//creates a temp pointer to the new node
	stackNode<float>* tempNode = new stackNode<float>(uData);

	//incriments the nodeCount variable by one
	nodeCount++;

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

float linkedFloatStack::pop()
{
	//checks if the stack is empty
	if (checkEmpty())
		return -999;

	//decriments Nodecount by one
	nodeCount--;

	//sets return value to the data value of the top node
	float returnValue = topNode->getData();

	//pointer to keep track of the top node
	stackNode<float>* tempNode = topNode;

	//sets the top node to the next node in the stack
	topNode = topNode->getNodeLink();

	//delete current topnode
	delete tempNode;

	//returns data value of the previous top node
	return returnValue;
}

float linkedFloatStack::peek()
{
	if (checkEmpty())
		return -999;
	else
		return topNode->getData();
}

//string linked stack class
class linkedStringStack
{
private:
	stackNode<std::string>* topNode;
public:
	linkedStringStack();
	bool checkEmpty();
	void push(std::string uData);
	std::string pop();
	std::string peek();
	void printStack();
	stackNode<std::string>* getTopNode();
};

linkedStringStack::linkedStringStack()
{
	topNode = 0;
}

stackNode<std::string>* linkedStringStack::getTopNode()
{
	return topNode;
}

//returns true if empty
bool linkedStringStack::checkEmpty()
{
	return topNode == 0;
}

void linkedStringStack::push(std::string uData)
{
	//creates a temp pointer to the new node
	stackNode<std::string>* tempNode = new stackNode<std::string>(uData);

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

std::string linkedStringStack::pop()
{
	if (checkEmpty())
		return "empty";

	//sets return value to the data value of the top node
	std::string returnValue = topNode->getData();

	//pointer to keep track of the top node
	stackNode<std::string>* tempNode = topNode;

	//sets the top node to the next node in the stack
	topNode = topNode->getNodeLink();

	//delete current topnode
	delete tempNode;

	//returns data value of the previous top node
	return returnValue;
}

std::string linkedStringStack::peek()
{
	if (checkEmpty())
		return "empty";
	else
		return topNode->getData();
}

//linked list class
class linkedList
{
private:
	linkedListNode *topNode;
public:
	linkedList();
	bool checkEmpty();
	void add(std::string uVarName, float uVarValue, int uScopeLevel, int uScopeLevelInstance[]);
	linkedListNode* searchList(std::string uVarName, int uScopeLevel, int uScopeLevelInstance[]);
	linkedListNode* getTopNode();
	void setTopNode(linkedListNode *uTopNode);
};

//default constructor, sets topNode to null
linkedList::linkedList()
{
	topNode = 0;
}

//returns topNode pointer
linkedListNode* linkedList::getTopNode()
{
	return topNode;
}

//setter for topNode
void linkedList::setTopNode(linkedListNode *uTopNode)
{
	topNode = uTopNode;
}

//returns true if empty
bool linkedList::checkEmpty()
{
	return topNode == 0;
}

//adds a node to the list
void linkedList::add(std::string uVarName, float uVarValue, int uScopeLevel, int uScopeLevelInstance[])
{
	//creates a temp pointer to the new node
	linkedListNode* tempNode = new linkedListNode(uVarName, uVarValue, uScopeLevel, uScopeLevelInstance);

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

//function that searches through the linked list and returns a pointer to the linkedListNode class object
//if the searchString does not exist in the list, returns a nullPointer
linkedListNode* linkedList::searchList(std::string uVarName, int uScopeLevel, int uScopeLevelInstance[])
{
	//bool that keeps track of whether the current var matching varName is in scope
	bool inScope = false;

	//sets the node* used to search the list to the topNode
	linkedListNode *tempSearchNode = topNode;

	if (tempSearchNode != 0)
	{
		//if-else block preforming the search
		while (true)
		{
			if (tempSearchNode->getVarName() == uVarName)
			{
				if (tempSearchNode->getScopeLevel() == 0)
					inScope = true;
				else
					if (tempSearchNode->getScopeLevel() == uScopeLevel && tempSearchNode->getScopeLevelInstance(uScopeLevel) == uScopeLevelInstance[uScopeLevel])
						inScope = true;
					else
					{
						bool externalVar = true;

						for (int i = 0; i < uScopeLevel; i++)
						{
							if (uScopeLevelInstance[i] != tempSearchNode->getScopeLevelInstance(i))
								inScope = false;
						}

						if (tempSearchNode->getScopeLevel() < uScopeLevel && externalVar)
							inScope = true;
					}
			}

			if (inScope)
				return tempSearchNode;
			else
				if (tempSearchNode->getNodeLink() != 0)
					tempSearchNode = tempSearchNode->getNodeLink();
				else
					return 0;
		}
	}
	else
		return 0;
}

//hash tabe class
class HashTable
{
private:
	linkedList hashTableArray[numArrayElements];
public:
	HashTable();
	linkedListNode* findVar(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[]);
	void assighnment(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[], float uVarValue = 0);
	bool incriment(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[]);
	bool decriment(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[]);
};

//default constructor for hashtable class
HashTable::HashTable()
{}

//function to return a pointer to a linkedListNode class object, returns null if there are no matches to the searchString
linkedListNode* HashTable::findVar(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[])
{
	linkedListNode *returnNode = hashTableArray[hash(uVarName)].searchList(uVarName, uScopeLevel, uScopeLevelInstances);

	if (returnNode != 0)
		return returnNode;
	else
		return 0;
}

//function that incriments the var associated with the name passed in
bool HashTable::incriment(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[])
{
	//creates a tempNode and assighns the correct node
	linkedListNode *tempNode = findVar(uVarName, uScopeLevel, uScopeLevelInstances);

	//incriments the varValue of the node or variable
	if (tempNode != 0)
	{
		tempNode->setVarValue(tempNode->getVarValue() + 1);
		return true;
	}
	else
		return false;
}

//function that decriments the var associated with the name passed in
bool HashTable::decriment(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[])
{
	//creates a tempNode and assighns the node Associated with the string
	linkedListNode* tempNode = findVar(uVarName, uScopeLevel, uScopeLevelInstances);

	//incriments the varValue of the node or variable
	if (tempNode != 0)
	{
		tempNode->setVarValue(tempNode->getVarValue() - 1);
		return true;
	}
	else
		return false;
}

//function that assighns a varValue to the node associated with varName variable
void HashTable::assighnment(std::string uVarName, int uScopeLevel, int uScopeLevelInstances[], float uVarValue)
{
	//adds the has key/value pair into the table if it doesnt allready exist within a given scope, if it does exist, updates the value
	if (findVar(uVarName, uScopeLevel, uScopeLevelInstances) == 0)
		hashTableArray[hash(uVarName)].add(uVarName, uVarValue, uScopeLevel, uScopeLevelInstances);
	else
		if (uScopeLevel == 0)
		{
			if (findVar(uVarName, uScopeLevel, uScopeLevelInstances) != 0)
			{
				findVar(uVarName, uScopeLevel, uScopeLevelInstances)->setScopeLevel(0);
				findVar(uVarName, uScopeLevel, uScopeLevelInstances)->setVarValue(uVarValue);
			}
			else
				hashTableArray[hash(uVarName)].add(uVarName, uVarValue, uScopeLevel, uScopeLevelInstances);
		}
		else
			findVar(uVarName, uScopeLevel, uScopeLevelInstances)->setVarValue(uVarValue);
}

//preforms a basic calculation
float basicCalc(float uVal1, float uVal2, std::string uOperator);

//returns true if the string contains digits
bool checkString(const std::string &testString);

//returns true if operator 1 has greater prescidence that operator 2
bool checkPrecedence(std::string uOperator1, std::string uOperator2);

//function used to evaluate expressions
float evaluateExpression(HashTable &uHashTable, std::string uExpression, int uScopeLevel, int uScopeLevelInstances[]);

//recursive funciton used to create scopes
void mainInterpreterFunction(HashTable &uHashTable, std::ifstream &uFileObject);

int main()
{
	//declares hashTable object
	HashTable hashTable;

	//opens input file
	std::ifstream inputFileObject("C:\\Users\\Richard\\Desktop\\Application Stuff\\Files\\Data Structrues Project 4\\BORGinput.txt");

	mainInterpreterFunction(hashTable, inputFileObject);

	std::cout << std::endl;

	std::cout << "Execution Completed" << std::endl;
}

//hash function
int hash(std::string uVarName)
{
	//sets the return hashValue to 0
	int returnHashValue = 0;

	//sums based on specified function
	for (int i = 0; i < uVarName.size(); i++)
	{
		returnHashValue = (int(uVarName.at(i))*(i + 1));
	}

	//preforms the modulo and returns the hashed value
	return returnHashValue % numArrayElements;
}

//function used to evaluate expressions
float evaluateExpression(HashTable &uHashTable, std::string uExpression, int uScopeLevel, int uScopeLevelInstances[])
{
	//declares the two stacks that will be used
	linkedFloatStack valueStack;
	linkedStringStack operatorStack;

	int j = 0, i = 0;

	float tempValue1, tempValue2;

	std::string tempString1, tempString2;

	//'parses' the first string
	while (j < uExpression.size() && uExpression.at(j) != ' ')
		j++;

	tempString1 = uExpression.substr(i, j - i);

	while (j < uExpression.size() + 1)
	{
		if (checkString(tempString1))
			valueStack.push(stof(tempString1));
		else
			if (tempString1 != "+" && tempString1 != "-" && tempString1 != "*" && tempString1 != "/" && tempString1 != "^")
			{
				if (uHashTable.findVar(tempString1, uScopeLevel, uScopeLevelInstances) != 0)
					valueStack.push(uHashTable.findVar(tempString1, uScopeLevel, uScopeLevelInstances)->getVarValue());
				else
					return -999;
			}
			else
			{
				//checks if the operator stack is not empty and if the operator prescidence of the operator on the 
				//top of the stack has the same or greater prescience than the current tempString operator
				while (!(operatorStack.checkEmpty()) && checkPrecedence(operatorStack.peek(), tempString1))
				{
					tempString2 = operatorStack.pop();

					tempValue2 = valueStack.pop();
					tempValue1 = valueStack.pop();

					valueStack.push(basicCalc(tempValue1, tempValue2, tempString2));
				}

				operatorStack.push(tempString1);
			}

		i = j + 1;
		j = i;

		if (j < uExpression.size())
		{
			//'parses' the the next string
			while (j < uExpression.size() && uExpression.at(j) != ' ')
				j++;

			tempString1 = uExpression.substr(i, j - i);
		}
	}

	while (!operatorStack.checkEmpty())
	{
		tempString2 = operatorStack.pop();

		tempValue2 = valueStack.pop();
		tempValue1 = valueStack.pop();

		valueStack.push(basicCalc(tempValue1, tempValue2, tempString2));
	}

	//returns the result
	return valueStack.pop();
}

//function used to simulate scope
void mainInterpreterFunction(HashTable &uHashTable, std::ifstream &uFileObject)
{
	std::string currentLine;

	//declares intergers used to keep track of scope
	int scopeLevel = 0;
	int scopeLevelInstance[maxNumScopeInstances];

	//sets all scopeLevelInstance elements to zero by default
	for (int j = 0; j < maxNumScopeInstances; j++)
		scopeLevelInstance[j] = 0;

	//stores the line into the currentLine string 
	getline(uFileObject, currentLine);

	//sets counting var to 0
	int i = 0;

	//skips any whitespace or /t
	if (currentLine != "")
		while (currentLine.at(i) == ' ' || currentLine.at(i) == '\t')
			i++;

	//main while loop
	while (!uFileObject.eof())
	{
		//enters a new scope if requested
		if (currentLine.substr(i, 5) == "START")
			scopeLevelInstance[++scopeLevel]++;
		else
			if (currentLine.substr(i, 6) == "FINISH")
				scopeLevel--;
			else
				if (currentLine.substr(i, 3) == "COM")
				{
				}
				else
					if (currentLine.substr(i, 3) == "VAR")
					{
						std::string tempExpressionVar, tempVarName;

						//collects the variable name and stores it in a tempVar
						i = i + 4;
						int j = i;

						while (currentLine.at(j) != ' ')
							j++;

						tempVarName = currentLine.substr(i, j - i);

						//shifts i past the = and any whitespace in front of the expression
						while (currentLine.at(i) != '=')
							i++;

						i = i + 1;

						while (currentLine.at(i) == ' ')
							i++;

						//assighns the rest of the string to the expression string
						tempExpressionVar = currentLine.substr(i, currentLine.size() - i);

						//adds the Key Value pair to the HashTable
						uHashTable.assighnment(tempVarName, scopeLevel, scopeLevelInstance, evaluateExpression(uHashTable, tempExpressionVar, scopeLevel, scopeLevelInstance));
					}
					else
						if (currentLine.substr(i, 5) == "PRINT")
						{
							float expressionValue;
							std::string tempExpressionVar;

							i = i + 5;

							//skips any whitespace between PRINT and expression substring
							while (currentLine.at(i) == ' ')
								i++;

							//string that holds the expression that will be evaluated
							tempExpressionVar = currentLine.substr(i, currentLine.size() - i);

							//evaluates the expression
							expressionValue = evaluateExpression(uHashTable, tempExpressionVar, scopeLevel, scopeLevelInstance);

							//if one of the variables wasnt undefined output evaluated result
							if (expressionValue != -999)
								std::cout << tempExpressionVar << " is " << expressionValue << std::endl;
							else
								std::cout << tempExpressionVar << " is undefined" << std::endl;
						}
						else
							if (currentLine.back() == '+' || currentLine.back() == '-')
							{
								int j = i;

								while (currentLine.at(j) != ' ')
									j++;

								if (uHashTable.findVar(currentLine.substr(i, j - i), scopeLevel, scopeLevelInstance) != 0)
								{
									if (currentLine.back() == '+')
										uHashTable.incriment(currentLine.substr(i, j - i), scopeLevel, scopeLevelInstance);
									else
										if (currentLine.back() == '-')
											uHashTable.decriment(currentLine.substr(i, j - i), scopeLevel, scopeLevelInstance);
								}
								else
									std::cout << currentLine.substr(i, j - i) << " is undefined" << std::endl;
							}
							else
							{
								std::string tempVarName;
								int j = i;

								while (currentLine.at(j) != ' ')
									j++;

								tempVarName = currentLine.substr(i, j - i);

								while (currentLine.at(i) != '=')
									i++;

								i = i + 1;

								while (currentLine.at(i) == ' ')
									i++;

								//stores the current variable as a global var
								uHashTable.assighnment(tempVarName, 0, scopeLevelInstance, evaluateExpression(uHashTable, currentLine.substr(i, currentLine.size() - i), scopeLevel, scopeLevelInstance));
							}

		//grabs another line
		getline(uFileObject, currentLine);

		//resets the counting var
		i = 0;

		//outputs currentLine before proccessed
		//std::cout << "Current Line: " << currentLine << std::endl;

		//skips any whitespace or /t
		if (currentLine != "")
			while (currentLine.at(i) == ' ' || currentLine.at(i) == '\t')
				i++;
	}
}

//preforms a basic calculation
float basicCalc(float uVal1, float uVal2, std::string uOperator)
{
	if (uOperator == "+")
		return uVal1 + uVal2;
	else
		if (uOperator == "-")
			return uVal1 - uVal2;
		else
			if (uOperator == "/")
				return uVal1 / uVal2;
			else
				if (uOperator == "*")
					return uVal1 * uVal2;
				else
					if (uOperator == "^")
						return pow(uVal1, uVal2);
					else
						return -999;
}

//returns true if the string contains only digits
bool checkString(const std::string &testString)
{
	return testString.find_first_not_of("0123456789") == std::string::npos;
}

//returns true if operator 1 has the same or greater prescidence that operator 2
bool checkPrecedence(std::string uOperator1, std::string uOperator2)
{
	int uVal1, uVal2;

	if (uOperator1 == "+" || uOperator1 == "-")
		uVal1 = 1;
	else
		if (uOperator1 == "*" || uOperator1 == "/")
			uVal1 = 2;
		else
			if (uOperator1 == "^")
				uVal1 = 3;

	if (uOperator2 == "+" || uOperator2 == "-")
		uVal2 = 1;
	else
		if (uOperator2 == "*" || uOperator2 == "/")
			uVal2 = 2;
		else
			if (uOperator2 == "^")
				uVal2 = 3;

	return uOperator1 >= uOperator2;
}

//BORAMIR is 25
//LEGOLAS is 101
//GANDALF is undefined
//BORAMIR * 2 is 52
//GANDALF is 49
//BORAMIR is 26
//GANDALF is undefined
//LEGOLAS is 1000
//LEGOLAS is 1000
//LEGOLAS is 999
//
//Execution Completed
//Press any key to continue . . .