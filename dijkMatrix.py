#array based Dijkstra's using an adj. matrix 
def dijkstra_matrix(matrix, src):
    V = len(matrix)
    dist = [float('inf')] * V
    visited = [False] * V
    dist[src] = 0

    for _ in range(V):
        # Find the unvisited vertex with smallest tentative distance
        min_dist = float('inf')
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        # Relax neighbors
        for v in range(V):
            if matrix[u][v] != 0 and not visited[v]:
                if dist[u] + matrix[u][v] < dist[v]:
                    dist[v] = dist[u] + matrix[u][v]
    return dist

"""
#TESTING
if __name__ == "__main__":
    # Dense Graph 1
    # Mapping: A=0, B=1, C=2, D=3, E=4
    dense1 = [
        [0, 2, 5, 1, 4],  # A
        [2, 0, 3, 2, 6],  # B
        [5, 3, 0, 3, 1],  # C
        [1, 2, 3, 0, 2],  # D
        [4, 6, 1, 2, 0]   # E
    ]

    result = dijkstra_matrix(dense1, 0)
    print(result)
"""
