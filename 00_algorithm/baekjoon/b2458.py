# https://www.acmicpc.net/problem/2458
# 키 순서

from collections import deque

q = deque()
N, M = map(int, input().split())
G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
S = [[set() for _ in range(2)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    G[a][b] = 1
result = 0
for i in range(1, N + 1):
    q.append(i)
    S[i][0].add(i)
    while len(q):
        v = q.popleft()
        for j in range(N + 1):
            if j not in S[i][0] and G[v][j] == 1:
                if len(S[j][0]) == 0:
                    S[i][0].add(j)
                    q.append(j)
                else:
                    S[i][0] |= S[j][0]
    q.append(i)
    S[i][1].add(i)
    while len(q):
        v = q.popleft()
        for j in range(N + 1):
            if j not in S[i][1] and G[j][v] == 1:
                if len(S[j][1]) == 0:
                    S[i][1].add(j)
                    q.append(j)
                else:
                    S[i][1] |= S[j][1]
for i in range(1, N + 1):
    if len(S[i][0]) + len(S[i][1]) - 1 == N:
        result += 1
print(result)
