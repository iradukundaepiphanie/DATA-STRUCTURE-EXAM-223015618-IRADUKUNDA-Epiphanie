#include <iostream>
#include <cstring>
using namespace std;

struct Edge {
    int to;
    float weight;
};

struct Vertex {
    int id;
    Edge* edges = nullptr;
    int edgeCount = 0, edgeCap = 0;
};

class GraphBase {
protected:
    Vertex* vertices = nullptr;
    int vertexCount = 0;

    Vertex* findVertex(int id) {
        for (int i = 0; i < vertexCount; ++i)
            if (vertices[i].id == id) return &vertices[i];
        return nullptr;
    }

    void insertEdge(Vertex* v, int to, float weight) {
        if (v->edgeCount >= v->edgeCap) {
            int newCap = v->edgeCap == 0 ? 2 : v->edgeCap * 2;
            Edge* newEdges = new Edge[newCap];
            memcpy(newEdges, v->edges, v->edgeCount * sizeof(Edge));
            delete[] v->edges;
            v->edges = newEdges;
            v->edgeCap = newCap;
        }
        *(v->edges + v->edgeCount) = {to, weight};
        v->edgeCount++;
    }

public:
    virtual ~GraphBase() {
        for (int i = 0; i < vertexCount; ++i) delete[] vertices[i].edges;
        delete[] vertices;
    }

    virtual void addEdge(int from, int to, float weight) = 0;

    void addVertex(int id) {
        Vertex* newVerts = new Vertex[vertexCount + 1];
        for (int i = 0; i < vertexCount; ++i) newVerts[i] = vertices[i];
        newVerts[vertexCount].id = id;
        delete[] vertices;
        vertices = newVerts;
        vertexCount++;
    }

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

    void print() {
        for (int i = 0; i < vertexCount; ++i) {
            cout << vertices[i].id << ": ";
            for (int j = 0; j < vertices[i].edgeCount; ++j)
                cout << "(" << (vertices[i].edges + j)->to << ", " << (vertices[i].edges + j)->weight << ") ";
            cout << endl;
        }
    }
};

class DirectedGraph : public GraphBase {
public:
    void addEdge(int from, int to, float weight) override {
        Vertex* v = findVertex(from);
        if (v) insertEdge(v, to, weight);
    }
};

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

int main() {
    GraphBase** graphs = new GraphBase*[2];
    graphs[0] = new DirectedGraph();
    graphs[1] = new BidirectionalGraph();

    for (int i = 0; i < 2; ++i) {
        graphs[i]->addVertex(1);
        graphs[i]->addVertex(2);
        graphs[i]->addVertex(3);
    }

    graphs[0]->addEdge(1, 2, 1.5f);
    graphs[1]->addEdge(1, 3, 2.0f);

    cout << "Directed:\n"; graphs[0]->print();
    cout << "Bidirectional:\n"; graphs[1]->print();

    delete graphs[0];
    delete graphs[1];
    delete[] graphs;
    return 0;
}
