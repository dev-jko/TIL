# https://www.acmicpc.net/problem/16235
# 나무 재테크

dxy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
tree = [list(map(int, input().split())) for _ in range(M)]
data = [[[5, []] for _ in range(N)] for _ in range(N)]
for x, y, z in tree:
    data[x - 1][y - 1][1].append(z)
for i in range(K):
    for x in range(N):
        for y in range(N):
            e = 0
            idx = 0
            for i in range(len(data[x][y][1])):
                if data[x][y][1][i] <= data[x][y][0]:
                    data[x][y][0] -= data[x][y][1][i]
                    data[x][y][1][i] += 1
                    idx += 1
                else:
                    e += data[x][y][1][i] // 2
            data[x][y][0] += e
            for i in range(len(data[x][y][1]) - idx):
                data[x][y][1].pop()
    for x in range(N):
        for y in range(N):
            data[x][y][0] += A[x][y]
            cnt = 0
            for z in data[x][y][1]:
                if z % 5 == 0:
                    cnt += 1
            if cnt > 0:
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        data[nx][ny][1] = [1] * cnt + data[nx][ny][1]
result = 0
for i in range(N):
    for j in range(N):
        result += len(data[i][j][1])
print(result)
