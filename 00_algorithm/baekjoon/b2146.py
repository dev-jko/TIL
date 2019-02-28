# TODO  실패
from collections import deque

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def grouping(m, n, group):
    data[m][n] = group
    for d in dxy:
        nx, ny = m + d[0], n + d[1]
        if m > 0 and data[nx][ny] == 1:
            grouping(nx, ny, group)


N = int(input())
data = []
v = [[False for _ in range(N)] for _ in range(N)]
d = [[99 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    data.append(list(map(int, input().split())))
group = 2
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            grouping(i, j, group)
            group += 1
for i in range(N):
    for j in range(N):
        pass
result = 100000

print(result)
