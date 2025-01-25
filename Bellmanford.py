def bellman_ford(graph, start, end):
    #initializing distances to all nodes as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # As distance from start node to itself is 0
    
    #predecessors to track the shortest path (dynamic programming)
    predecessors = {node: None for node in graph}
    
    #relaxing edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph.get(node, {}).items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
    
    #checking for negative cycles
    for node in graph:
        for neighbor, weight in graph.get(node, {}).items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative cycle")
    
    #constructing the shortest path
    shortest_path = []
    node = end  #starting from the destination node
    while node is not None:
        shortest_path.insert(0, node)
        node = predecessors[node]
    
    return distances, shortest_path
