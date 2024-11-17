n, m = map(int, input().split())
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
maze = []
for row in range(n):
    maze.append(list(map(int, input().split())))
visited = set()
pos = (0, 0)
goal = (n-1, m-1)
dfs = [pos]
answer = False
while dfs:
    x, y = dfs.pop()
    visited.add((x, y))
    for dx, dy in directions:
        x += dx
        y += dy
        if (x, y) == goal:
            answer = True
            break
        if (x, y) not in visited and (0 <= x < n and 0 <= y <m) and maze[x][y] != 0:
            dfs.append((x, y))
print("1" if answer else "0")