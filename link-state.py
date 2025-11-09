# Program: Link State Routing using Dijkstra's Algorithm

# Graph represented as adjacency matrix
graph = [
    [0, 2, 0, 1, 0],
    [2, 0, 3, 2, 0],
    [0, 3, 0, 0, 1],
    [1, 2, 0, 0, 3],
    [0, 0, 1, 3, 0]
]

num_nodes = len(graph)

start = int(input("Enter Source Node (0-4): "))

dist = [float('inf')] * num_nodes
visited = [False] * num_nodes

dist[start] = 0

for _ in range(num_nodes):
    # Select node with minimum distance not yet visited
    min_dist = float('inf')
    for i in range(num_nodes):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            current = i

    visited[current] = True

    # Update distances of adjacent nodes
    for j in range(num_nodes):
        if graph[current][j] != 0 and not visited[j]:
            if dist[current] + graph[current][j] < dist[j]:
                dist[j] = dist[current] + graph[current][j]

print("\nShortest Distance from Node", start)
for i in range(num_nodes):
    print("To Node", i, ":", dist[i])
