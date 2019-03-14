# https://www.acmicpc.net/problem/2660
# 회장뽑기

from collections import deque

q = deque()
N = int(input())
G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    G[a][b] = G[b][a] = 1
S = [0 for _ in range(N + 1)]
S[0] = 9999
visited = [-1 for _ in range(N + 1)]
for i in range(1, N + 1):
    visited[i] = 0
    q.append(i)
    while len(q):
        v = q.popleft()
        for j in range(1, N + 1):
            if G[v][j] == 1 and visited[j] == -1:
                visited[j] = visited[v] + 1
                q.append(j)
    S[i] = max(visited)
    for j in range(1, N + 1):
        visited[j] = -1
result = [min(S), []]
for i in range(1, N + 1):
    if S[i] == result[0]:
        result[1].append(i)
print(result[0], len(result[1]))
print(*result[1])
