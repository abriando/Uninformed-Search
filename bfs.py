# BFS algorithm in Python

# BFS algorithm
graph = {
  '1' : ['4','2'],
  '4' : ['3'],
  '3' : ['10','9'],
  '2' : ['5','7','8'],
  '5' : ['6']
}

visited = []
queue = []     

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

bfs(visited, graph, '1')