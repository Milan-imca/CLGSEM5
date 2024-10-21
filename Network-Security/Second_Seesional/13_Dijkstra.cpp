#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

typedef pair<int, int> pii; // First: distance, Second: node

// Dijkstra's Algorithm function
void dijkstra(int source, vector<vector<pii>>& graph, vector<int>& dist) {
    priority_queue<pii, vector<pii>, greater<pii>> pq; // Min-heap (priority queue)

    dist[source] = 0;
    pq.push({0, source}); // {distance, node}

    while (!pq.empty()) {
        int d = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        // Skip processing if we've found a better way to u
        if (d > dist[u]) continue;

        // Visit each neighbor v of u
        for (auto& neighbor : graph[u]) {
            int v = neighbor.second;
            int weight = neighbor.first;

            // Relaxation step
            if (dist[u] + weight < dist[v]) {
                dist[v] = dist[u] + weight;
                pq.push({dist[v], v});
            }
        }
    }
}

int main() {
    int n, m, source;

    cout << "Enter the number of nodes and edges: ";
    cin >> n >> m;

    vector<vector<pii>> graph(n);
    vector<int> dist(n, INT_MAX); // Distance from source to each node, initialized to infinity

    cout << "Enter the edges (u, v, weight) for each edge:" << endl;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph[u].push_back({w, v});
        graph[v].push_back({w, u}); // Uncomment if the graph is undirected
    }

    cout << "Enter the source node: ";
    cin >> source;

    // Run Dijkstra's algorithm
    dijkstra(source, graph, dist);

    // Output the shortest distance to each node from the source
    cout << "Shortest distances from node " << source << ":" << endl;
    for (int i = 0; i < n; i++) {
        if (dist[i] == INT_MAX)
            cout << "Node " << i << ": Unreachable" << endl;
        else
            cout << "Node " << i << ": " << dist[i] << endl;
    }

    return 0;
}


/* sample output 
Enter the number of nodes and edges: 5 6
Enter the edges (u, v, weight) for each edge:
0 1 10
0 4 5
1 2 1
1 4 2
2 3 4
3 4 9
Enter the source node: 0


Shortest distances from node 0:
Node 0: 0
Node 1: 7
Node 2: 8
Node 3: 12
Node 4: 5

*/