import time

def measure_performance(flow_function, *args):
    """
    Measure the time and output of a flow function.
    """
    start_time = time.time()
    flow_value = flow_function(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return flow_value, elapsed_time

def print_metrics(method_name, flow_value, elapsed_time):
    """
    Print performance metrics for an algorithm.
    """
    print(f"{method_name} Results:")
    print(f"Total Flow: {flow_value}")
    print(f"Execution Time: {elapsed_time:.6f} seconds\n")

# Example of usage
if __name__ == "__main__":
    from baseline_comparisons import greedy_baseline, shortest_path_baseline
    
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

    # Measure performance for Greedy Baseline
    greedy_flow, greedy_time = measure_performance(greedy_baseline, flow_network, source, sink)
    print_metrics("Greedy Baseline", greedy_flow, greedy_time)

    # Measure performance for Shortest Path Baseline
    shortest_flow, shortest_time = measure_performance(shortest_path_baseline, flow_network, source, sink)
    print_metrics("Shortest Path Baseline", shortest_flow, shortest_time)
