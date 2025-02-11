import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Algorithmus Berechnung des MST
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
np.random.seed(42)  # Seed zum Reproduzieren
positions = {i: np.random.rand(3) for i in range(n)} 

edges = [(i, j, np.linalg.norm(positions[i] - positions[j])) for i in range(n) for j in range(i + 1, n)]
mst_edges = kruskal(n, edges)

G = nx.Graph()
G.add_weighted_edges_from(edges)

fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(121, projection='3d')
ax.set_title("Originalgraph")

for u, v, w in edges:
    x_vals, y_vals, z_vals = zip(positions[u], positions[v])
    ax.plot(x_vals, y_vals, z_vals, 'gray', alpha=0.5)

for node, pos in positions.items():
    ax.scatter(*pos, color='blue', s=100)
    ax.text(*pos, str(node), color='black', fontsize=12)

ax = fig.add_subplot(122, projection='3d')
ax.set_title("Minimum Spanning Tree (MST)")

for u, v, w in mst_edges:
    x_vals, y_vals, z_vals = zip(positions[u], positions[v])
    ax.plot(x_vals, y_vals, z_vals, 'red', linewidth=2)

for node, pos in positions.items():
    ax.scatter(*pos, color='green', s=100)
    ax.text(*pos, str(node), color='black', fontsize=12)

plt.show()
