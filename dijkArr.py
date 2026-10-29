import randGraph #for generating random dense adj list
#Haley Gray

def dijkstra_array(adj, src):
    V = len(adj)
    dist = [float('inf')] * V
    visited = [False] * V

    dist[src] = 0

    for _ in range(V):
        # Find the unvisited vertex with the smallest tentative distance
        min_dist = float('inf')
        u = -1
        for i in range(V):
            if not visited[i] and dist[i] < min_dist:
                min_dist = dist[i]
                u = i

        if u == -1:          # all remaining vertices are unreachable
            break

        visited[u] = True

        # Relax all outgoing edges from u
        for v, w in adj[u]:
            if not visited[v] and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist

"""
if __name__ == "__main__":
    src = 0

    #Sparse graph 1
    # Mapping: A=0, B=1, C=2, D=3, E=4, F=5
    adjsg1 = [
        [(1, 4), (2, 2)],   # A -> B (4), A -> C (2)
        [(3, 5)],           # B -> D (5)
        [(3, 1)],           # C -> D (1)
        [(4, 3)],           # D -> E (3)
        [(5, 2)],           # E -> F (2)
        []                  # F has no outgoing edges
    ]
    #Sparse graph 2
    # Mapping: 1->0, 2->1, 3->2, 4->3, 5->4, 6->5, 7->6
    adjsg2 = [
        [(1, 3), (2, 6)],   # 1 -> 2 (3), 1 -> 3 (6)
        [(3, 2), (4, 5)],   # 2 -> 4 (2), 2 -> 5 (5)
        [(4, 4)],           # 3 -> 5 (4)
        [(5, 7)],           # 4 -> 6 (7)
        [(6, 1)],           # 5 -> 7 (1)
        [],                 # 6 has no outgoing edges
        []                  # 7 has no outgoing edges
    ]

    #Dense graph 1
    # Mapping: A=0, B=1, C=2, D=3, E=4
    adjdg1 = [
        [(1, 2), (2, 5), (3, 1), (4, 4)],   # A -> B(2), C(5), D(1), E(4)
        [(0, 2), (2, 3), (3, 2), (4, 6)],   # B -> A(2), C(3), D(2), E(6)
        [(0, 5), (1, 3), (3, 3), (4, 1)],   # C -> A(5), B(3), D(3), E(1)
        [(0, 1), (1, 2), (2, 3), (4, 2)],   # D -> A(1), B(2), C(3), E(2)
        [(0, 4), (1, 6), (2, 1), (3, 2)]    # E -> A(4), B(6), C(1), D(2)
    ]
    #Dense graph 2
    # Mapping: 1->0, 2->1, 3->2, 4->3, 5->4, 6->5
    adjdg2 = [
        [(1, 3), (2, 2), (3, 6), (4, 5), (5, 4)],   # 1 -> (2,3), (3,2), (4,6), (5,5), (6,4)
        [(0, 3), (2, 1), (3, 2), (4, 4), (5, 7)],   # 2 -> (1,3), (3,1), (4,2), (5,4), (6,7)
        [(0, 2), (1, 1), (3, 3), (4, 6), (5, 5)],   # 3 -> (1,2), (2,1), (4,3), (5,6), (6,5)
        [(0, 6), (1, 2), (2, 3), (4, 2), (5, 4)],   # 4 -> (1,6), (2,2), (3,3), (5,2), (6,4)
        [(0, 5), (1, 4), (2, 6), (3, 2), (5, 1)],   # 5 -> (1,5), (2,4), (3,6), (4,2), (6,1)
        [(0, 4), (1, 7), (2, 5), (3, 4), (4, 1)]    # 6 -> (1,4), (2,7), (3,5), (4,4), (5,1)
    ]
    #use rand. generated Dense graph (100)
    adjdgRand = randGraph.generate_dense_adj_list(100, density=0.9)


    #result = dijkstra_array(adj, src)
    #print(result)  # Output: [0, 4, 7, 9, 10]
"""
