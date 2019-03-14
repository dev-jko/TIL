# https://www.acmicpc.net/problem/2589
# 보물섬

from collections import deque

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]

q = deque()
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(input()))
D = [[-1 for _ in range(M)] for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if data[i][j] == 'W':
            continue
        for ti in range(N):
            for tj in range(M):
                D[ti][tj] = -1
        q.append((i, j))
        D[i][j] = 0
        while len(q):
            x, y = q.popleft()
            for dx, dy in dxy:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 'L' and D[nx][ny] == -1:
                    D[nx][ny] = D[x][y] + 1
                    q.append((nx, ny))
                    result = max(result, D[nx][ny])
print(result)

