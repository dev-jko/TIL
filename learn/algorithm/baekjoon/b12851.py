# https://www.acmicpc.net/problem/12851
# 숨바꼭질 2

from collections import deque

q = deque()
N, K = map(int, input().split())
data = [-1 for _ in range(100001)]
cnt = 0
q.append((K, 0))
data[K] = 0
while len(q):
    x, t = q.popleft()
    if x == N and data[x] == t:
        cnt += 1
        continue
    next_cnt = data[x] + 1
    if 1 <= x and (data[x - 1] == -1 or data[x - 1] == t + 1):
        data[x - 1] = next_cnt
        q.append((x - 1, t + 1))
    if x + 1 <= 100000 and (data[x + 1] == -1 or data[x + 1] == t + 1):
        data[x + 1] = next_cnt
        q.append((x + 1, t + 1))
    if x % 2 == 0 and (data[x // 2] == -1 or data[x // 2] == t + 1):
        data[x // 2] = next_cnt
        q.append((x // 2, t + 1))
print(data[N], cnt, sep='\n')
