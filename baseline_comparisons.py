import networkx as nx

def greedy_baseline(flow_network, source, sink):
    """
    Greedy algorithm that tries to push flow sequentially, not considering overall optimality.
    """
    G = nx.DiGraph(flow_network)
    flow_value = 0
    path = nx.shortest_path(G, source, sink, weight=None)
    for edge in zip(path, path[1:]):
        flow_value += G[edge[0]][edge[1]]['capacity']
    return flow_value

def shortest_path_baseline(flow_network, source, sink):
    """
    Shortest path method to find a simple route without considering max flow.
    """
    G = nx.DiGraph(flow_network)
    path = nx.shortest_path(G, source, sink, weight=None)
    flow_value = sum(G[u][v]['capacity'] for u, v in zip(path[:-1], path[1:]))
    return flow_value

# Example usage
if __name__ == "__main__":
    # Example network
    flow_network = {
        0: {1: {'capacity': 16}, 2: {'capacity': 13}},
        1: {2: {'capacity': 10}, 3: {'capacity': 12}},
        2: {1: {'capacity': 4}, 4: {'capacity': 14}},
        3: {2: {'capacity': 9}, 5: {'capacity': 20}},
        4: {3: {'capacity': 7}, 5: {'capacity': 4}},
    }
    source = 0
    sink = 5

    greedy_flow = greedy_baseline(flow_network, source, sink)
    print(f"Greedy baseline flow: {greedy_flow}")

    shortest_path_flow = shortest_path_baseline(flow_network, source, sink)
    print(f"Shortest path baseline flow: {shortest_path_flow}")
