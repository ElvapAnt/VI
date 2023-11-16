import queue


def bfs_tree_height(graph, start):
    queue_nodes = queue.Queue()
    queue_nodes.put((start, 0))
    visited = set()
    visited.add(start)

    max_level = 0

    while not queue_nodes.empty():
        node, level = queue_nodes.get()
        max_level = max(max_level, level)

        # Explore the neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue_nodes.put((neighbor, level + 1))

    return max_level


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G'],
    'G': []
}

start_node = 'A'
tree_height = bfs_tree_height(graph, start_node)
print("The height of the search tree is:", tree_height)
