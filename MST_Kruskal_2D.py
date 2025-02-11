import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])  
    parent = list(range(n))
    
    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    mst = []
    for u, v, w in edges:
        root_u, root_v = find(u), find(v)
        if root_u != root_v:
            mst.append((u, v, w))
            parent[root_u] = root_v
        if len(mst) == n - 1:
            break
    return mst

n = 20
np.random.seed(42)  # Seed für reproduzierbare Ergebnisse
positions = {i: np.random.rand(2) for i in range(n)}  

edges = [(i, j, np.linalg.norm(positions[i] - positions[j])) for i in range(n) for j in range(i + 1, n)]
mst_edges = kruskal(n, edges)

G = nx.Graph()
G.add_weighted_edges_from(edges)

plt.figure(figsize=(10, 5))
plt.title("Minimum Spanning Tree (MST) - 2D Visualisierung")

for u, v, w in edges:
    x_vals, y_vals = zip(positions[u], positions[v])
    plt.plot(x_vals, y_vals, 'gray', alpha=0.2) 

for u, v, w in mst_edges:
    x_vals, y_vals = zip(positions[u], positions[v])
    plt.plot(x_vals, y_vals, 'red', linewidth=2) 
for node, pos in positions.items():
    plt.scatter(*pos, color='blue', s=50)
    plt.text(*pos, str(node), fontsize=8, color='black', ha='right')

plt.show()
