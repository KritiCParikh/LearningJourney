# Graphs

## 1. **Definition**
A **Graph** is a non-linear data structure that consists of a collection of nodes (also called vertices) and edges (connections between nodes). It is used to represent relationships or connections between various objects. Graphs are widely used in modeling scenarios like social networks, road maps, and computer networks.

- **Vertex (Node):** An individual entity in the graph.
- **Edge (Link):** A connection or relationship between two vertices. It can be directed (one-way) or undirected (two-way).

## 2. **Types of Graphs**
Graphs can be classified based on the characteristics of the edges and vertices.

- **Directed Graph (Digraph):** The edges have a direction, meaning they go from one vertex to another. For example, a Twitter following relation where a user follows another user.
  
- **Undirected Graph:** The edges have no direction, meaning the relationship between vertices is mutual. For example, a friendship network where both users are friends.

- **Weighted Graph:** Each edge has a weight or cost associated with it. This can represent the distance between cities or the time required to travel from one location to another.

- **Unweighted Graph:** The edges do not have any weights or costs. All edges are treated the same.

- **Cyclic Graph:** A graph that contains at least one cycle (a path that starts and ends at the same vertex).

- **Acyclic Graph:** A graph that does not contain any cycles. A Directed Acyclic Graph (DAG) is one example, where edges have directions, and there are no cycles.

- **Connected Graph:** A graph where there is a path between every pair of vertices (in undirected graphs).

- **Disconnected Graph:** A graph where at least two vertices do not have a path between them (in undirected graphs).

- **Tree:** A special type of graph where there are no cycles, and there is exactly one path between any two vertices. A tree is a connected acyclic graph.

## 3. **Operations on Graphs**
The fundamental operations that can be performed on a graph include:

- **Traversal:**
  - **Breadth-First Search (BFS):** A level-by-level traversal of the graph starting from a given node. It is used for finding the shortest path in unweighted graphs.
  - **Depth-First Search (DFS):** A depth-first traversal where you explore as far as possible along each branch before backtracking. It is used for pathfinding, cycle detection, and topological sorting.

- **Insertion:** Adding a new vertex or an edge to the graph.
  
- **Deletion:** Removing a vertex or an edge from the graph.

- **Find Path:** Determining whether a path exists between two vertices.
  
- **Shortest Path:** Finding the shortest path between two vertices, often using algorithms like Dijkstra’s or Bellman-Ford.

- **Cycle Detection:** Checking whether a graph contains a cycle.

- **Topological Sorting:** Ordering vertices of a Directed Acyclic Graph (DAG) such that for every directed edge \( u \to v \), vertex \( u \) comes before vertex \( v \).

## 4. **Implementation of Graphs**
Graphs can be implemented using two main structures:

- **Adjacency Matrix:**
  - A 2D array is used to represent a graph, where a cell at position \( (i, j) \) contains a value (often 1 or the weight) if there is an edge from vertex \( i \) to vertex \( j \), otherwise 0 (or infinity for weighted graphs).
  - **Advantages:** Efficient for dense graphs (graphs with many edges).
  - **Disadvantages:** Consumes more space, especially for sparse graphs (graphs with fewer edges).

- **Adjacency List:**
  - A collection of lists or hashmaps, where each vertex has a list of all the vertices it is connected to. It’s a more space-efficient way to represent a graph.
  - **Advantages:** More space-efficient for sparse graphs.
  - **Disadvantages:** It can be slower for checking if an edge exists between two vertices (O(V) time complexity).

- **Edge List:**
  - A simple list where each element is a pair (or tuple) of vertices that form an edge in the graph. This is typically used when only the edges are important (e.g., for graph algorithms like Kruskal’s for minimum spanning trees).
  
## 5. **Common Problems Involving Graphs**

- **Shortest Path Algorithms:**
  - **Dijkstra’s Algorithm:** Finds the shortest path from a source vertex to all other vertices in a weighted graph with non-negative weights.
  - **Bellman-Ford Algorithm:** Computes the shortest paths from a source vertex to all other vertices in a weighted graph, allowing for negative weights (but no negative weight cycles).
  
- **Cycle Detection:**
  - In a directed graph, you can use DFS with recursion stacks to detect cycles.
  - In an undirected graph, DFS or BFS can also be used with parent pointers to detect cycles.
  
- **Topological Sorting (for Directed Acyclic Graphs):** Given a DAG, find an ordering of vertices such that for every directed edge \( u \to v \), vertex \( u \) comes before vertex \( v \).

- **Connected Components:** Find all the connected components in an undirected graph.

- **Graph Coloring:** Assign colors to the vertices of a graph such that no two adjacent vertices share the same color. This is useful in problems like scheduling.

- **Minimum Spanning Tree (MST):**
  - **Kruskal’s Algorithm:** A greedy algorithm for finding the MST of a graph.
  - **Prim’s Algorithm:** Another greedy algorithm for finding the MST by growing the tree one edge at a time.

- **Bipartite Graph Checking:** A graph is bipartite if the vertices can be divided into two sets such that no two vertices within the same set share an edge.

- **Strongly Connected Components:** In a directed graph, a Strongly Connected Component (SCC) is a subgraph where every vertex is reachable from every other vertex in that subgraph.

## 6. **CRUD Operations in Graphs**

- **Create:**
  - Create a new graph by defining its structure (adjacency matrix, adjacency list, etc.).
  - Add a vertex or an edge.

- **Read:**
  - Access and view the vertices and edges.
  - Perform graph traversal (DFS/BFS).
  - Query properties like whether a path exists between two vertices.

- **Update:**
  - Modify an existing edge (e.g., change the weight).
  - Update the graph structure (e.g., add new vertices or edges).
  
- **Delete:**
  - Remove a vertex or an edge from the graph.
  - Delete a vertex and all its edges.
 
## 7. **Implementation**

There are two common ways to represent a graph in computer science:

1. **Adjacency Matrix**: A 2D array of size V x V where V is the number of vertices. Each element `matrix[i][j]` holds a value that indicates whether there is an edge between vertex `i` and vertex `j`.

2. **Adjacency List**: A dictionary or list where each vertex has a list of adjacent vertices. This representation is more space-efficient for sparse graphs.


## Graph Implementation (Adjacency List Representation)

```python
class Graph:
    def __init__(self):
        # Initialize an empty adjacency list
        self.graph = {}

    # Add a directed edge from u to v
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    # Add an undirected edge between u and v
    def add_undirected_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    # BFS Traversal (Breadth-First Search)
    def bfs(self, start):
        visited = set()  # Track visited nodes
        queue = [start]  # Start with the given node
        visited.add(start)

        bfs_traversal = []

        while queue:
            node = queue.pop(0)  # Pop the first element in the queue
            bfs_traversal.append(node)

            # Add unvisited neighbors to the queue
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return bfs_traversal

    # DFS Traversal (Depth-First Search)
    def dfs(self, start):
        visited = set()  # Track visited nodes
        dfs_traversal = []

        # Helper function for DFS recursion
        def dfs_helper(node):
            visited.add(node)
            dfs_traversal.append(node)
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)

        # Start DFS traversal from the given node
        dfs_helper(start)
        return dfs_traversal

# Example Usage:
g = Graph()

# Add directed edges
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Add an undirected edge
g.add_undirected_edge(4, 5)

# BFS and DFS Traversal
print("BFS starting from node 0:", g.bfs(0))  # Expected output: [0, 1, 2, 3, 4, 5]
print("DFS starting from node 0:", g.dfs(0))  # Expected output: [0, 1, 3, 4, 5, 2]

```

References: https://www.youtube.com/watch?v=4jyESQDrpls
