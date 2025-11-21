# Breadth first search Algorithm
# Example: Determine the adjacency list in the following graphVertices dictionary 
# Undirected graph
#        A
#     /  \  \
#    B    C   D
#    | \  |   
#    E    F

GraphVertices = {
    'A' : ['B' , 'C' ,'D'],
    'B' : ['A', 'E','F'],
    'C' : ['A' , 'F'],
    'D' : ['A'],
    'E' : ['B'],
    'F' : ['B' , 'C']
}

Algorithm = 'bfs'

goalState =''
visited = []
frontier =[]
import sys

def DoSearch(visited, GraphVertices, currentNode):
    visited.append(currentNode)
    frontier.append(currentNode)

    while frontier:
        if Algorithm == 'bfs':
            m =frontier.pop(0) #queue
        else:
            m= frontier.pop()  #stack

        print(m, "->")

        for adjacent in GraphVertices[m]:
            if adjacent not in visited:
                visited.append(adjacent)
                frontier.append(adjacent)

    return visited


# --- Main ---
Algorithm = Algorithm.lower()
if Algorithm not in ['bfs', 'dfs']:
    sys.exit('Please Determine the Algorithm')

txt = 'Depth-First' if Algorithm =='dfs' else 'Breadth-First'
if(goalState == ''):
    print(f'The {txt} Traversal order of the graph is:')
else:
    print(f'The {txt} search order of the graph is:')
print(DoSearch(visited, GraphVertices, 'A'))



