import networkx as nx
import matplotlib.pyplot as plt

def visualize_flow_network(flow_network, title="Flow Network"):
    """
    Visualize the flow network using matplotlib and networkx.
    """
    G = nx.DiGraph(flow_network)
    pos = nx.spring_layout(G)
    capacities = nx.get_edge_attributes(G, 'capacity')
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=capacities)
    plt.title(title)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Example network (same as before)
    flow_network = {
        0: {1: {'capacity': 16}, 2: {'capacity': 13}},
        1: {2: {'capacity': 10}, 3: {'capacity': 12}},
        2: {1: {'capacity': 4}, 4: {'capacity': 14}},
        3: {2: {'capacity': 9}, 5: {'capacity': 20}},
        4: {3: {'capacity': 7}, 5: {'capacity': 4}},
    }

    visualize_flow_network(flow_network, "Initial Flow Network")
