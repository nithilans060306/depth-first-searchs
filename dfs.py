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