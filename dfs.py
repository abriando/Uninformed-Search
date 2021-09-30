# DFS algorithm in Python

# DFS algorithm
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'1': set(['4']),
         '4': set(['3']),
         '3': set(['10','9','2']),
         '2': set(['8']),
         '8': set(['7']),
         '7': set(['5']),
         '5': set(['6'])}

dfs(graph, '1')