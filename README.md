# Experiment No. 2: Implement Depth First Search (DFS) Traversal of a Graph  

## Name: Nithilan S  
## Register Number: 212223240108  

## Aim:  
To implement Depth First Search (DFS) traversal of a graph using Python 3.  

## Theory:  
**Depth First Search (DFS)** for a graph is similar to DFS for a tree. However, unlike trees, graphs may contain cycles, meaning a node can be visited more than once. To avoid processing the same node multiple times, we use a Boolean `visited` array.  

A graph can have multiple DFS traversals. DFS starts at an arbitrary node (or root node in case of a tree) and explores as far as possible along each branch before backtracking.  

### **DFS Steps:**  
1. Initially, the stack and visited arrays are empty.  
2. Visit the start node and push its unvisited adjacent nodes into the stack.  
3. Pop the top node from the stack, visit it, and push its unvisited adjacent nodes.  
4. Repeat the process until the stack is empty.  

## Algorithm:  
1. Construct a graph with nodes and edges.  
2. DFS uses a **stack** (explicit or recursion).  
3. Insert the **start node** into the stack.  
4. Check its **successors** (neighboring nodes).  
5. If a node is **not visited**, add it to the stack and continue.  
6. Continue this process until no more nodes need to be visited.  

---

## Program:  
```python
from collections import defaultdict

def dfs(graph, start, visited, path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:  
            dfs(graph, neighbour, visited, path)  
    return path

graph = defaultdict(list)
n, e = map(int, input().split())  
for i in range(e):
    u, v = input().split()  
    graph[u].append(v)  
    graph[v].append(u)  

start = list(graph.keys())[0]  
visited = defaultdict(bool)
path = []
print("Sample Output:")
traversed_path = dfs(graph, start, visited, path)
print(traversed_path)
```


## Sample Input:

8 9 <BR>
A B <BR>
A C <BR>
B E <BR>
C D <BR>
B D <BR>
C G <BR>
D F <BR>
G F <BR>
F H <BR>
## Sample Output:
['A', 'B', 'E', 'D', 'C', 'G', 'F', 'H']

<hr>

## Sample Input:

5 5 <BR>
0 1 <BR>
0 2 <BR>
0 3 <BR>
2 3 <BR>
2 4 <BR>
## Sample Output:

['0', '1', '2', '3', '4']

## Result:

<p>Thus,a Graph was constructed and implementation of Depth First Search for the same graph was done successfully.</p>

