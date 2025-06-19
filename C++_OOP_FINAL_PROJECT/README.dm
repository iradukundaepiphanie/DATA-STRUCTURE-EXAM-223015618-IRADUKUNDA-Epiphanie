ASSIGNED TASK:

Design a C++ program using Object-Oriented Programming (OOP) principles to implement a graph system that supports:
Dynamic addition/removal of vertices.
Directed and bidirectional (undirected) edges.
Dynamic edge storage using memory management.
Base and derived class usage with polymorphism.

HOW IT WAS COMPLETED:

Structures: Used Vertex and Edge structs to define graph elements.
Base Class GraphBase: Handles shared logic like adding/removing vertices and edges.
Derived Classes: DirectedGraph and BidirectionalGraph override the addEdge() method with specific logic.
Dynamic Arrays: Vertices and their edges use manual memory allocation and resizing.
Polymorphism: Managed both graph types via a base pointer for flexibility.

  ANNOTATED CODE:

  #include <iostream>  // For input/output
#include <cstring>   // For memory operations (memcpy)
using namespace std;

// Edge between two vertices with a weight
struct Edge {
    int to;
    float weight;
};

// Represents a vertex with dynamic list of edges
struct Vertex {
    int id;
    Edge* edges = nullptr;  // Pointer to edges
    int edgeCount = 0, edgeCap = 0;  // Dynamic size control
};

// Abstract base class for graphs
class GraphBase {
protected:
    Vertex* vertices = nullptr;
    int vertexCount = 0;

    // Find a vertex by ID
    Vertex* findVertex(int id) {
        for (int i = 0; i < vertexCount; ++i)
            if (vertices[i].id == id) return &vertices[i];
        return nullptr;
    }

    // Add an edge to a vertex, resizing if needed
    void insertEdge(Vertex* v, int to, float weight) {
        if (v->edgeCount >= v->edgeCap) {
            int newCap = v->edgeCap == 0 ? 2 : v->edgeCap * 2;
            Edge* newEdges = new Edge[newCap];
            memcpy(newEdges, v->edges, v->edgeCount * sizeof(Edge));
            delete[] v->edges;
            v->edges = newEdges;
            v->edgeCap = newCap;
        }
        *(v->edges + v->edgeCount) = {to, weight};  // Add edge
        v->edgeCount++;
    }

public:
    // Clean up dynamic memory
    virtual ~GraphBase() {
        for (int i = 0; i < vertexCount; ++i) delete[] vertices[i].edges;
        delete[] vertices;
    }

    // Abstract method for adding edges
    virtual void addEdge(int from, int to, float weight) = 0;

    // Add a new vertex
    void addVertex(int id) {
        Vertex* newVerts = new Vertex[vertexCount + 1];
        for (int i = 0; i < vertexCount; ++i) newVerts[i] = vertices[i];
        newVerts[vertexCount].id = id;
        delete[] vertices;
        vertices = newVerts;
        vertexCount++;
    }

    // Remove a vertex by ID
    void removeVertex(int id) {
        int idx = -1;
        for (int i = 0; i < vertexCount; ++i)
            if (vertices[i].id == id) idx = i;
        if (idx == -1) return;
        delete[] vertices[idx].edges;
        Vertex* newVerts = new Vertex[vertexCount - 1];
        for (int i = 0, j = 0; i < vertexCount; ++i)
            if (i != idx) newVerts[j++] = vertices[i];
        delete[] vertices;
        vertices = newVerts;
        vertexCount--;
    }

    // Print the graph (vertex + its edges)
    void print() {
        for (int i = 0; i < vertexCount; ++i) {
            cout << vertices[i].id << ": ";
            for (int j = 0; j < vertices[i].edgeCount; ++j)
                cout << "(" << (vertices[i].edges + j)->to << ", " << (vertices[i].edges + j)->weight << ") ";
            cout << endl;
        }
    }
};

// Directed graph adds edge one-way
class DirectedGraph : public GraphBase {
public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v = findVertex(from);
        if (v) insertEdge(v, to, weight);
    }
};

// Bidirectional graph adds edge both ways
class BidirectionalGraph : public GraphBase {
public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v1 = findVertex(from), *v2 = findVertex(to);
        if (v1 && v2) {
            insertEdge(v1, to, weight);
            insertEdge(v2, from, weight);
        }
    }
};

// Main function to test the graphs
int main() {
    GraphBase** graphs = new GraphBase*[2];
    graphs[0] = new DirectedGraph();       // Create directed graph
    graphs[1] = new BidirectionalGraph();  // Create bidirectional graph

    // Add vertices to both graphs
    for (int i = 0; i < 2; ++i) {
        graphs[i]->addVertex(1);
        graphs[i]->addVertex(2);
        graphs[i]->addVertex(3);
    }

    // Add directed and bidirectional edges
    graphs[0]->addEdge(1, 2, 1.5f);  // Directed: 1 -> 2
    graphs[1]->addEdge(1, 3, 2.0f);  // Bidirectional: 1 <-> 3

    // Output both graphs
    cout << "Directed:\n"; graphs[0]->print();
    cout << "Bidirectional:\n"; graphs[1]->print();

    // Clean up
    delete graphs[0];
    delete graphs[1];
    delete[] graphs;
    return 0;
}
