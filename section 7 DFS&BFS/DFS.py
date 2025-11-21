# Depth First Search Algorithm
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
# The priority of reading a graph in default is from left to right
DirPrior = '' # or DirPrior = 'ltr' -> from left to write (default)
#DirPrior = 'rtl' -> from right to left
#DirPrior = 'alpha' -> Alphabetical
goalState =''
def DFS(GraphVertices,initialState , visited = None):
    if visited is None:
        visited = []
    visited.append(initialState)

    for adjacent  in GraphVertices[initialState]:
        if adjacent not in visited:
            DFS(GraphVertices , adjacent ,visited)
    return visited

DirPrior = DirPrior.lower()
if DirPrior != 'rtl' and DirPrior !='alpha':DirPrior = 'ltr'
if DirPrior == 'rtl':
    for v in GraphVertices:
        GraphVertices[v].reverse()

if DirPrior == 'alpha':
    for v in GraphVertices:
        GraphVertices[v].sort()

if(goalState == ''):
    print('The depth first traversal order ltr')
else:
    print('The depth first traversal order rtl')

print(DFS(GraphVertices,'A'))

