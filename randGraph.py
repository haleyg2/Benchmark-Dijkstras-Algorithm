import random


def generate_dense_graph(V, density=0.8, min_weight=1, max_weight=10):
    """
    Returns (adj_list, adj_matrix) for the same undirected dense graph.
    """
    INF = float('inf')
    adj_list = [[] for _ in range(V)]
    adj_matrix = [[INF] * V for _ in range(V)]
    for i in range(V):
        adj_matrix[i][i] = 0                       # distance to self

    for i in range(V):
        for j in range(i + 1, V):                  # undirected, process each pair once
            if random.random() < density:
                w = random.randint(min_weight, max_weight)
                # Append to adjacency list (both directions)
                adj_list[i].append((j, w))
                adj_list[j].append((i, w))
                # Set matrix entries (symmetric)
                adj_matrix[i][j] = w
                adj_matrix[j][i] = w
    return adj_list, adj_matrix
