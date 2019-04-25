# https://www.acmicpc.net/problem/2636
# 치즈

from collections import deque


def bfs(t, air):
    q.clear()
    q.append((t, t))
    c = set({})
    while len(q):
        x, y = q.popleft()
        for d in dxy:
            nx, ny = x + d[0], y + d[1]
            if 0 + t <= nx < N - t and 0 + t <= ny < M - t:
                if data[nx][ny] == 0 or data[nx][ny] == (-2 if air == -1 else -1):
                    data[nx][ny] = air
                    q.append((nx, ny))
                elif data[nx][ny] == 1 and (nx, ny) not in c:
                    c.add((nx, ny))
    result = len(c)
    for x, y in c:
        data[x][y] = air
    return result


dxy = [[0, -1], [0, 1], [-1, 0], [1, 0]]
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
t = 0
cnt = temp = 0
air = -1
data[0][0] = air
q = deque()
while True:
    cnt = temp
    temp = bfs(t, air)
    t += 1
    air = -2 if air == -1 else -1
    if temp == 0:
        break
print('{}\n{}'.format(t - 1, cnt))
