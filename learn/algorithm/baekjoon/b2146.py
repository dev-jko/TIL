from collections import deque

dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def dfs():
    group = 2
    s = deque()
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                s.append((i, j))
                data[i][j] = group
                D[i][j] = 0
                while len(s):
                    x, y = s.pop()
                    for d in dxy:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 1:
                            data[nx][ny] = group
                            D[nx][ny] = 0
                            s.append((nx, ny))
                group += 1


def bfs():
    result = 9999
    q = deque()
    for i in range(N):
        for j in range(N):
            if data[i][j] != 0:
                q.append((i, j))
    while len(q):
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 <= nx < N and 0 <= ny < N:
                if D[nx][ny] == -1:
                    D[nx][ny] = D[x][y] + 1
                    data[nx][ny] = data[x][y]
                    q.append((nx, ny))
                elif data[x][y] != data[nx][ny]:
                    if D[x][y] == D[nx][ny]:
                        result = min(result, D[x][y] + D[x][y])
                    else:
                        result = min(result, D[x][y] + D[nx][ny])
    return result


N = int(input())
data = []
D = [[-1 for _ in range(N)] for _ in range(N)]
for _ in range(N):
    data.append(list(map(int, input().split())))
dfs()
print(bfs())
