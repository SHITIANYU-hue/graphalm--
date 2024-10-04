import networkx as nx
from evaluation_metrics import measure_performance, print_metrics

def edmonds_karp_max_flow(flow_network, source, sink):
    """
    Edmonds-Karp algorithm to compute maximum flow.
    """
    G = nx.DiGraph(flow_network)
    flow_value, _ = nx.maximum_flow(G, source, sink, flow_func=nx.algorithms.flow.edmonds_karp)
    return flow_value

def push_relabel_max_flow(flow_network, source, sink):
    """
    Push-Relabel algorithm to compute maximum flow.
    """
    G = nx.DiGraph(flow_network)
    flow_value, _ = nx.maximum_flow(G, source, sink, flow_func=nx.algorithms.flow.preflow_push)
    return flow_value

# Example of usage
if __name__ == "__main__":
    # Example network (same as before)
    flow_network = {
        0: {1: {'capacity': 16}, 2: {'capacity': 13}},
        1: {2: {'capacity': 10}, 3: {'capacity': 12}},
        2: {1: {'capacity': 4}, 4: {'capacity': 14}},
        3: {2: {'capacity': 9}, 5: {'capacity': 20}},
        4: {3: {'capacity': 7}, 5: {'capacity': 4}},
    }
    source = 0
    sink = 5

    # Compare Edmonds-Karp
    ek_flow, ek_time = measure_performance(edmonds_karp_max_flow, flow_network, source, sink)
    print_metrics("Edmonds-Karp Max Flow", ek_flow, ek_time)

    # Compare Push-Relabel
    pr_flow, pr_time = measure_performance(push_relabel_max_flow, flow_network, source, sink)
    print_metrics("Push-Relabel Max Flow", pr_flow, pr_time)
