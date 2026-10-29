import time, tracemalloc
import dijk #heap implementation input:(adj list)
import dijkArr #array implementation input:(adj list)
import dijkMatrix #ONLY ARRAY implementation (Matrix)
import randGraph #generate random dense graph


def benchmark(dijk_func, adj, src, trials=5):
    times = []
    mems = []
    for _ in range(trials):
        tracemalloc.start()
        t0 = time.perf_counter()
        result = dijk_func(adj, src)
        t1 = time.perf_counter()
        _, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        times.append((t1 - t0) * 1000)  # ms
        mems.append(peak / 1024**2)     # MB
    avg_time = sum(times)/len(times)
    avg_mem = sum(mems)/len(mems)
    return avg_time, avg_mem, result

def verify_distances(adj_list, src, dist):
    """Check that dist array is a valid shortest-path solution for an undirected graph."""
    V = len(adj_list)
    if dist[src] != 0:
        return False, "Source distance not zero"
    for u in range(V):
        for v, w in adj_list[u]:
            if dist[v] > dist[u] + w + 1e-9:   # tiny epsilon for floating error
                return False, f"Edge ({u},{v}) weight {w}"
    # If graph is connected (you can pass a flag), ensure no inf
    # if connected and any(d == float('inf') for d in dist):
    #    return False, "Unreachable vertex in connected graph"
    return True, "OK"

#INPUTS--------------------
#--------------------------
#Sparse graph 1
# Mapping: A=0, B=1, C=2, D=3, E=4, F=5
adj_listsg1 = [
    [(1, 4), (2, 2)],   # A -> B (4), A -> C (2)
    [(3, 5)],           # B -> D (5)
    [(3, 1)],           # C -> D (1)
    [(4, 3)],           # D -> E (3)
    [(5, 2)],           # E -> F (2)
    []                  # F has no outgoing edges
]
#Sparse graph 2
# Mapping: 1->0, 2->1, 3->2, 4->3, 5->4, 6->5, 7->6
adj_listsg2 = [
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
adj_listdg1 = [
    [(1, 2), (2, 5), (3, 1), (4, 4)],   # A -> B(2), C(5), D(1), E(4)
    [(0, 2), (2, 3), (3, 2), (4, 6)],   # B -> A(2), C(3), D(2), E(6)
    [(0, 5), (1, 3), (3, 3), (4, 1)],   # C -> A(5), B(3), D(3), E(1)
    [(0, 1), (1, 2), (2, 3), (4, 2)],   # D -> A(1), B(2), C(3), E(2)
    [(0, 4), (1, 6), (2, 1), (3, 2)]    # E -> A(4), B(6), C(1), D(2)
]
#Dense graph 1 as adj Matrix
adj_matrixdg1 = [
    # A   B   C   D   E
    [  0,  2,  5,  1,  4],   # A
    [  2,  0,  3,  2,  6],   # B
    [  5,  3,  0,  3,  1],   # C
    [  1,  2,  3,  0,  2],   # D
    [  4,  6,  1,  2,  0]    # E
]
#Dense graph 2
# Mapping: 1->0, 2->1, 3->2, 4->3, 5->4, 6->5
adj_listdg2 = [
    [(1, 3), (2, 2), (3, 6), (4, 5), (5, 4)],   # 1 -> (2,3), (3,2), (4,6), (5,5), (6,4)
    [(0, 3), (2, 1), (3, 2), (4, 4), (5, 7)],   # 2 -> (1,3), (3,1), (4,2), (5,4), (6,7)
    [(0, 2), (1, 1), (3, 3), (4, 6), (5, 5)],   # 3 -> (1,2), (2,1), (4,3), (5,6), (6,5)
    [(0, 6), (1, 2), (2, 3), (4, 2), (5, 4)],   # 4 -> (1,6), (2,2), (3,3), (5,2), (6,4)
    [(0, 5), (1, 4), (2, 6), (3, 2), (5, 1)],   # 5 -> (1,5), (2,4), (3,6), (4,2), (6,1)
    [(0, 4), (1, 7), (2, 5), (3, 4), (4, 1)]    # 6 -> (1,4), (2,7), (3,5), (4,4), (5,1)
]
adj_matrixdg2 = [
    # 1   2   3   4   5   6
    [ 0,  3,  2,  6,  5,  4],   # 1
    [ 3,  0,  1,  2,  4,  7],   # 2
    [ 2,  1,  0,  3,  6,  5],   # 3
    [ 6,  2,  3,  0,  2,  4],   # 4
    [ 5,  4,  6,  2,  0,  1],   # 5
    [ 4,  7,  5,  4,  1,  0]    # 6
]
src = 0
print("Source vertex =",src)


#Benchmark inputs----------------------
#--------------------------------------
print("========Starting Benchmarks========")

#dijk array on Sparse 1 (adj List)
avg_time, avg_mem, result1 = benchmark(dijkArr.dijkstra_array, adj_listsg1,src)
print("SG1 arr_vers. input_list: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result1)
#dijk Min heap on Sparse 1 (adj List)
avg_time, avg_mem, result2 = benchmark(dijk.dijkstra_heap, adj_listsg1,src)
print("SG1 heap_vers. input_list: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result2)
same_path = []
same_path.append(result1 == result2)
#verify min path cost by checking relaxation
ok, msg = verify_distances(adj_listsg1, src, result1)
print("SG1 distances valid?", ok, msg)
print()


#dijk array on Sparse 2 (adj List)
avg_time, avg_mem, result1 = benchmark(dijkArr.dijkstra_array, adj_listsg2,src)
print("SG2 arr_vers. input_list: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result1)
#dijk Min heap on Sparse 2 (adj List)
avg_time, avg_mem, result2 = benchmark(dijk.dijkstra_heap, adj_listsg2,src)
print("SG2 heap_vers. input_list: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result2)
same_path.append(result1 == result2)
#verify min path cost by checking relaxation
ok, msg = verify_distances(adj_listsg2, src, result1)
print("SG2 distances valid?", ok, msg)
print()



#dijk array on Dense 1 (adj Matrix)
avg_time, avg_mem, result1 = benchmark(dijkMatrix.dijkstra_matrix,adj_matrixdg1 ,src)
print("DG1 matrix_vers input_matrix: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result1)
#dijk Min heap on Dense 1 (adj List)
avg_time, avg_mem, result2 = benchmark(dijk.dijkstra_heap, adj_listdg1,src)
print("DG1 heap_vers input_list: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result2)
same_path.append(result1 == result2)
#verify min path cost by checking relaxation
ok, msg = verify_distances(adj_listdg1, src, result2)
print("DG1 distances valid?", ok, msg)
print()


#dijk array on Dense 2 (adj Matrix)
avg_time, avg_mem, result1 = benchmark(dijkMatrix.dijkstra_matrix, adj_matrixdg2,src)
print("DG2 matrix_vers input_matrix: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result1)
#dijk Min heap on Dense 2 (adj List)
avg_time, avg_mem, result2 = benchmark(dijk.dijkstra_heap, adj_listdg2,src)
print("DG2 heap_vers input_list: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result2)
same_path.append(result1 == result2)
#verify min path cost by checking relaxation
ok, msg = verify_distances(adj_listdg2, src, result2)
print("DG1 distances valid?", ok, msg)
print()



#RANDOM GENDERATED graph as (adj list) & (adj matrix)---------------
#use rand. generated Dense graph (500)   (Corresponding  list/matrix)
rand_adj_list, rand_adj_matrix = randGraph.generate_dense_graph(500, density=0.9)

#dijk array on Random Generated Dense 3 (adj Matrix)
avg_time, avg_mem, result1 = benchmark(dijkMatrix.dijkstra_matrix , rand_adj_matrix,src)
print("Dense graph 3-rand as matrix: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result1)
#dijk Min heap on Random Generated Dense 3 (adj List)
avg_time, avg_mem, result2 = benchmark(dijk.dijkstra_heap, rand_adj_list,src)
print("Dense graph 3-rand as list:: Time =",f"{avg_time:.4f}","Mem =",f"{avg_mem:.4f}","path =",result2)
same_path.append(result1 == result2)
#verify min path cost by checking relaxation
ok, msg = verify_distances(rand_adj_list, src, result2)
print("DG 3-rand distances valid?", ok, msg)


#verify each dijk. func outputs same path
if (all(same_path)):
    print("Same paths for each call")
else:
    print("Paths mismatch")
print("Finished Benchmarks")
