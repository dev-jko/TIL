#  https://www.acmicpc.net/problem/2206
# 벽 부수고 이동하기

from collections import deque

dxy = [[0, -1], [0, 1], [1, 0], [-1, 0]]


def bfs(m, n, D):
    global N, M, result
    for i in range(N):
        for j in range(M):
            D[i][j] = -1
    D[m][n] = 1
    q.append((m, n))
    while len(q):
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0 and D[nx][ny] == -1:
                D[nx][ny] = D[x][y] + 1
                q.append((nx, ny))


N, M = map(int, input().split())
q = deque()
data = []
for _ in range(N):
    data.append(list(map(int, input())))
Ds = [[-1 for _ in range(M)] for _ in range(N)]
De = [[-1 for _ in range(M)] for _ in range(N)]
result = 999999
bfs(0, 0, Ds)
bfs(N - 1, M - 1, De)
ws = []
for i in range(N):
    for j in range(M):
        cnt = 0
        if data[i][j] == 1:
            for d in dxy:
                nx, ny = i + d[0], j + d[1]
                if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0:
                    cnt += 1
            if cnt >= 2:
                ws.append((i, j))
if Ds[N - 1][M - 1] != -1 and De[0][0] == Ds[N - 1][M - 1]:
    result = De[0][0]
for w in ws:
    x, y = w
    min_s = 999999
    min_e = 999999
    for d in dxy:
        nx, ny = x + d[0], y + d[1]
        if 0 <= nx < N and 0 <= ny < M and data[nx][ny] == 0:
            if Ds[nx][ny] != -1:
                min_s = min(min_s, Ds[nx][ny])
            if De[nx][ny] != -1:
                min_e = min(min_e, De[nx][ny])
    result = min(result, min_s + min_e + 1)
if result >= 99999:
    result = -1
print(result)
