# https://www.acmicpc.net/problem/14502
#  연구소

from collections import deque


def bfs(w1, w2, w3):
    data_t = [[i for i in j] for j in data]
    data_t[blank[w1][0]][blank[w1][1]] = 1
    data_t[blank[w2][0]][blank[w2][1]] = 1
    data_t[blank[w3][0]][blank[w3][1]] = 1
    for i in range(N):
        for j in range(M):
            if data_t[i][j] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and data_t[nx][ny] == 0:
                data_t[nx][ny] = 2
                q.append((nx, ny))
    result = 0
    for i in data_t:
        result += i.count(0)
    return result


dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
q = deque()
blank = []
for i in range(N):
    for j in range(M):
        if data[i][j] == 0:
            blank.append((i, j))
select = [i for i in range(len(blank))]
result = 0
for i in range(len(select)):
    for j in range(i + 1, len(select)):
        for k in range(j + 1, len(select)):
            result = max(result, bfs(i, j, k))
print(result)
