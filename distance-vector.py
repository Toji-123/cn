# Program: Distance Vector Routing using Bellman-Ford Algorithm

INF = 999

# Cost matrix
graph = [
    [0, 2, INF, 1, INF],
    [2, 0, 3, 2, INF],
    [INF, 3, 0, INF, 1],
    [1, 2, INF, 0, 3],
    [INF, INF, 1, 3, 0]
]

num_nodes = len(graph)

# Distance table
dist = [row[:] for row in graph]

# Applying Bellman-Ford
for _ in range(num_nodes - 1):
    for i in range(num_nodes):
        for j in range(num_nodes):
            for k in range(num_nodes):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

print("\nDistance Vector Table:")
for i in range(num_nodes):
    print("Router", i, ":", dist[i])
