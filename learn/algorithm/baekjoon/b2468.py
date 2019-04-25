#  https://www.acmicpc.net/problem/2468
# 안전 영역

from collections import deque

dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = deque()
N = int(input())
data = []
max_height = 0
for _ in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)
    max_height = max(max_height, max(temp))
result = 1
for rain in range(1, max_height):
    group = 1
    G = [[-1 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if data[i][j] > rain and G[i][j] == -1:
                q.append((i, j))
                G[i][j] = group
                while len(q):
                    x, y = q.popleft()
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N and G[nx][ny] == -1 and data[nx][ny] > rain:
                            G[nx][ny] = group
                            q.append((nx, ny))
                group += 1
    result = max(result, group - 1)
print(result)
