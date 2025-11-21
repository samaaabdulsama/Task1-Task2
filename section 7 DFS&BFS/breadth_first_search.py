graph = {
  's' : ['w','r'],
  'w' : ['t', 'x'],
  'r' : ['v'],
  'v' : [],
  't' : ['u'],
  'x' : ['y'],
  'u' : [],
  'y' : []
}
# create two lists one for enqueue a visited node and another for looping to all node 
visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for Breadth first search 
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbor in graph[m]:
      if neighbor not in visited:
        visited.append(neighbor)
        queue.append(neighbor)

# function calling
bfs(visited, graph, 's')    