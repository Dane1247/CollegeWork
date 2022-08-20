#include <iostream>
#include <string>

//graph class that contains the matirx 
class Graph
{
private:
	bool **Matrix;
	std::string *vertexLabels;
	int numVertices;
public:
	Graph(int uNumVertices);
	void addEdge(std::string uSourceVertex, std::string uTargetVertex);
	void printEdges();
};

//constructor for graph class object, accepts the number of 
//vertices that space will be dynamically allocated for as an argument
Graph::Graph(int uNumVertices)
{
	//assighns the appropriate value to numVertices value
	numVertices = uNumVertices;

	//instatiates the graph matrix
	Matrix = new bool *[uNumVertices];
	for (int i = 0; i < uNumVertices; i++)
		Matrix[i] = new bool[uNumVertices];

	//sets all elements of the graph to false(0) by default
	for (int i = 0; i < uNumVertices; i++)
		for (int j = 0; j < uNumVertices; j++)
			Matrix[i][j] = false;

	vertexLabels = new std::string[uNumVertices];

	std::string tempString;

	//asks the user to label the vertices
	for (int i = 0; i < uNumVertices; i++)
	{
		std::cout << "Enter the Label for Vertex " << i + 1 << ": ";
		std::cin >> tempString;
		vertexLabels[i] = tempString;
	}
}

//adds an edge to the graph based on the strings passed in
void Graph::addEdge(std::string uSourceVertex, std::string uTargetVertex)
{
	//stores the interger associated with the string passed into function
	int sourceVertex, targetVertex;

	//stores whether the interger associated with the vertex has been found
	bool sourceVertexFound = false, targetVertexFound = false;

	//finds the interger associed with the string passed in and assighns it to the sourceVertex Var
	//stops searching if it has searched through all elements of the array of strings
	for (int i = 0; (!sourceVertexFound) && i < numVertices; i++)
	{
		if (uSourceVertex == vertexLabels[i])
		{
			sourceVertex = i;
			sourceVertexFound = true;
		}
	}

	for (int i = 0; (!targetVertexFound) && i < numVertices; i++)
	{
		if (uTargetVertex == vertexLabels[i])
		{
			targetVertex = i;
			targetVertexFound = true;
		}
	}

	//if both the sourcrVertex and targetVertex strings have an associated vertex, assighn the corresponding edge to true in the matrix
	if (sourceVertexFound && targetVertexFound)
		Matrix[sourceVertex][targetVertex] = true;
	else
		std::cout << "The Edge could not be Created, One or more of the Strings Entered was Invalid" << std::endl;
}

//Prints out all edges
void Graph::printEdges()
{
	std::cout << "Edges: ";

	//prints out all edges
	for (int i = 0; i < numVertices; i++)
		for (int j = 0; j < numVertices; j++)
			if (Matrix[i][j])
				std::cout << vertexLabels[i] << vertexLabels[j] << " ";
}

int main()
{
	//variables used to accept user input
	int uNumVertices;
	std::string uVertex1, uVertex2;
	bool uInputBool = true;

	std::cout << "Enter the Number of Vertices to Create in the Graph: ";
	std::cin >> uNumVertices;

	std::cout << std::endl;

	//instantiates the graph class object
	Graph graphObject(uNumVertices);
	
	std::cout << std::endl;

	//accepts user input used to create edges
	while (uInputBool)
	{
		std::cout << "Enter Two Vertices Between which to Create an Edge(Enter -1 to Stop): ";
		std::cin >> uVertex1;

		//checks if the user has entered the stop condition
		if (uVertex1 != "-1")
		{
			std::cin >> uVertex2;
			graphObject.addEdge(uVertex1, uVertex2);
		}
		else
			uInputBool = false;
	}

	std::cout << std::endl;

	//prints all edges
	graphObject.printEdges();

	std::cout << std::endl;
}