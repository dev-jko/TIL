# https://www.acmicpc.net/problem/16236
# 아기 상어

from collections import deque


class Baby:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = self.need = 2

    def move(self, x, y):
        self.x = x
        self.y = y
        self.need -= 1
        if self.need == 0:
            self.size += 1
            self.need = self.size


dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]
q = deque()
N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
baby = None
for i in range(N):
    for j in range(N):
        if data[i][j] == 9:
            baby = Baby(i, j)
            data[i][j] = 0
t = 0
while True:
    D = [[-1 for _ in range(N)] for _ in range(N)]
    D[baby.x][baby.y] = 0
    q.append((baby.x, baby.y))
    min_d = 999
    while len(q):
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N  and D[nx][ny] == -1:
                if data[nx][ny] == 0 or data[nx][ny] == baby.size:
                    if min_d >= D[x][y] + 1:
                        D[nx][ny] = D[x][y] + 1
                        q.append((nx, ny))
                elif data[nx][ny] < baby.size:
                    D[nx][ny] = D[x][y] + 1
                    min_d = D[nx][ny]
    d = 99
    next_pos = None
    for i in range(N):
        for j in range(N):
            if 0 < data[i][j] < baby.size and 0 < D[i][j] < d:
                d = D[i][j]
                next_pos = (i, j)
    if next_pos is None:
        break
    else:
        x, y = next_pos
        baby.move(x, y)
        t += d
        data[x][y] = 0
print(t)
