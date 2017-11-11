def get_triangle():
    r = []
    c = []
    with open('triangle.in') as f:
        for line in f:
            r.append([int(a) for a in line.strip().split(" ")])
            c.append([0 for _ in line.strip().split(" ")])
    return r, c


triangle, cost = get_triangle()

cost[0][0] = triangle[0][0]

for row in range(1, len(triangle)):
    cost[row][0] = cost[row-1][0] + triangle[row][0]
    cost[row][len(triangle[row])-1] = cost[row-1][len(triangle[row-1])-1] + triangle[row][len(triangle[row])-1]

for row in range(2, len(triangle)):
    for col in range(1, len(triangle[row])-1):
        cost[row][col] = triangle[row][col] + (cost[row-1][col-1] if cost[row-1][col-1] > cost[row-1][col] else cost[row-1][col])

print(max(cost[-1:][0]))
