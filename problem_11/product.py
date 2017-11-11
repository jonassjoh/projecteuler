def horizontal(grid, n):
    best = 0
    for i in range(len(grid)):
        for k in range(len(grid[i]) - n):
            s = 1
            for p in range(n):
                s *= int(grid[i][k+p])
            if s > best:
                best = s
    return best

def vertical(grid, n):
    best = 0
    for k in range(len(grid[0]) - n):
        for i in range(len(grid)):
            s = 1
            for p in range(n):
                s *= int(grid[k+p][i])
            if s > best:
                best = s
    return best

def diagonally(grid, n):
    best = 0
    for i in range(len(grid) - n):
        for k in range(len(grid[i]) - n):
            s = 1
            for p in range(n):
                s *= int(grid[i+p][k+p])
            if s > best:
                best = s
    return best

def diagonally2(grid, n):
    best = 0
    for i in range(len(grid) - n):
        for k in range(n-1, len(grid[i])):
            s = 1
            for p in range(n):
                s *= int(grid[i+p][k-p])
            if s > best:
                best = s
    return best

grid = []
with open('grid.in') as f:
    for line in f:
        line = line.strip().split(' ')
        grid.append(line)

best = horizontal(grid, 4)
t = vertical(grid, 4)
t2 = diagonally(grid, 4)
t3 = diagonally2(grid, 4)

best = best if best > t else t
best = best if best > t2 else t2
best = best if best > t3 else t3

print(best)
