# https://www.acmicpc.net/problem/1697
# 숨바꼭질

from collections import deque

N, K = map(int, input().split())
if N >= K:
    print(N - K)
else:
    data = [-1 for _ in range(100001)]
    q = deque()
    q.append(K)
    data[K] = 0
    while len(q):
        x = q.popleft()
        if x == N:
            break
        next_cnt = data[x] + 1
        if 1 <= x and data[x - 1] == -1:
            data[x - 1] = next_cnt
            q.append(x - 1)
        if x + 1 <= 100000 and data[x + 1] == -1:
            data[x + 1] = next_cnt
            q.append(x + 1)
        if x % 2 == 0 and data[x // 2] == -1:
            data[x // 2] = next_cnt
            q.append(x // 2)
    print(data[N])
