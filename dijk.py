import heapq
import sys
#Haley Gray

def dijkstra_heap(adj, src):

    V = len(adj)

    # Min-heap (priority queue) storing pairs of (distance, node)
    pq = []

    dist = [sys.maxsize] * V

    # Distance from source to itself is 0
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    # Process the queue until all reachable vertices are finalized
    while pq:
        d, u = heapq.heappop(pq)

        # If this distance not the latest shortest one, skip it
        if d > dist[u]:
            continue

        # Explore all neighbors of the current vertex
        for v, w in adj[u]:

            # If we found a shorter path to v through u, update it
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    # Return the final shortest distances from the source
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
