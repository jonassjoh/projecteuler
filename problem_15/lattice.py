grid = []

for i in range(20):
    grid.append([])
    for j in range(20):
        grid[i].append(0)

for i in range(20):
    grid[i][0] = i + 2
for i in range(20):
    grid[0][i] = i + 2

for i in range(1, 20):
    for j in range(1, 20):
        grid[i][j] = grid[i][j-1]
        grid[i][j] += grid[i-1][j]

for i in grid:
    print(i)
