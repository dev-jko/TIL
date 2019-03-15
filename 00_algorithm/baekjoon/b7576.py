# https://www.acmicpc.net/problem/7576
#  토마토

from collections import deque

q = deque()
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
M, N = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
D = [[-1 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if data[i][j] == 1:
            D[i][j] = 0
            q.append((i, j))
        if data[i][j] == -1:
            D[i][j] = 0
while len(q):
    x, y = q.popleft()
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0 and D[nx][ny] == -1:
            D[nx][ny] = D[x][y] + 1
            q.append((nx, ny))
result = 0
for arr in D:
    if arr.count(-1) > 0:
        print(-1)
        break
    result = max(result, max(arr))
else:
    print(result)
