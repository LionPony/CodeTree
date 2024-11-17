from collections import deque
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = set()
bfs = deque([1])
visited.add(1)

while bfs:
    node = bfs.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            bfs.append(neighbor)

print(len(visited) - 1)