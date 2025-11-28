import heapq

def dijkstra_with_path(graph, start_node, end_node=None):
    """
    Finds the shortest paths and predecessors from a start node.

    Returns:
        A tuple containing (distances dictionary, predecessors dictionary).
    """
    distances = {node: float('infinity') for node in graph}
    distances[start_node] = 0
    
    # Dictionary to store the immediate previous node on the shortest path from the start
    predecessors = {node: None for node in graph}
    
    priority_queue = [(0, start_node)] #distance , current node
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        # Optimization: If we only need one destination and we reached it, stop early
        if end_node is not None and current_node == end_node:
            break

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # Key addition: Update the grandparents for the neighbor
                predecessors[neighbor] = current_node   
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, predecessors

def reconstruct_path(predecessors, start_node, end_node):
    """
    Reconstructs the shortest path from the start to the end node using the predecessors map.
    """
    path = []
    current = end_node
    
    # Traverse backward from the end node to the start node
    while current is not None:
        path.append(current)
        current = predecessors[current]
        
        # Safety break if the path somehow doesn't lead back to the start
        if current == start_node:
            path.append(start_node)
            break
            
    # The path is built backward, so reverse it to get start -> end order
    path.reverse()
    
    # Handle cases where the end node is unreachable or invalid
    if path[0] != start_node or path[-1] != end_node:
        return [f"Path from {start_node} to {end_node} does not exist or is unreachable."]

    return path


my_graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1, 'E': 3},
    'E': {'D': 3, 'F': 2}, 
    'F': {'E': 2}
}

start_node = 'A'
end_node = 'F' # The destination you want the path for

# Run Dijkstra's algorithm
distances, predecessors = dijkstra_with_path(my_graph, start_node, end_node)

# Reconstruct the specific path
shortest_path = reconstruct_path(predecessors, start_node, end_node)
final_distance = distances[end_node]

print(f"Shortest distance from {start_node} to {end_node}: {final_distance}")
print(f"The shortest path is: {' -> '.join(shortest_path)}")

