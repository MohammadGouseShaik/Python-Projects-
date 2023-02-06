def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    unvisited_nodes = graph.keys()

    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)
        if distances[current_node] == float('inf'):
            break
        for neighbor, weight in graph[current_node].items():
            if weight + distances[current_node] < distances[neighbor]:
                distances[neighbor] = weight + distances[current_node]
                previous_nodes[neighbor] = current_node

    path = []
    current_node = end
    while previous_nodes[current_node] is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.insert(0, start)
    return path
