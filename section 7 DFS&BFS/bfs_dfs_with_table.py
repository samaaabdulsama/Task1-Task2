from collections import deque  # support FIFO

def bfs_with_table_and_order(graph, start):
    visited = []
    queue = deque([start])
    traversal_order = [] # STORE THE FINAL OUTPUT

    print(f"{'Current':<10}{'Queue':<20}{'Visited'}")
    print("-" * 45)

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            traversal_order.append(current)
            queue.extend([n for n in graph[current] if n not in visited and n not in queue])
        
        queue_str = ' '.join(queue)
        visited_str = ' '.join(visited)
        print(f"{current:<10}{queue_str:<20}{visited_str}")

    # Final state after traversal
    print(f"{'':<10}{'-':<20}{' '.join(visited)}")
    print("\nBreadth-First Traversal Order:", " -> ".join(traversal_order))

# Define the graph
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': [],
    'D': [],
    'E': [],
    'F': []
}

# Run BFS
bfs_with_table_and_order(graph, 'A')

# DFS with table + traversal order (using stack)
def dfs_with_table_and_order(graph, start):
    visited = []
    stack = [start]
    traversal_order = []

    print("\n--- Depth-First Search (DFS) ---")
    print(f"{'Current':<10}{'Stack':<20}{'Visited'}")
    print("-" * 45)

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            traversal_order.append(current)
            # Add neighbors in reverse so leftmost is visited first
            stack.extend(reversed([n for n in graph[current] if n not in visited]))
        
        stack_str = ' '.join(stack)
        visited_str = ' '.join(visited)
        print(f"{current:<10}{stack_str:<20}{visited_str}")

    print(f"{'':<10}{'-':<20}{' '.join(visited)}")
    print("\nDFS Traversal Order:", " -> ".join(traversal_order))


# Run DFS
dfs_with_table_and_order(graph, 'A')
