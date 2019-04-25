# https://www.acmicpc.net/problem/13913
# 숨바꼭질 4

from collections import deque

N, K = map(int, input().split())
data = [[-1, -1] for _ in range(100001)]
data[K][0] = 0
data[K][1] = K
q = deque()
q.append(K)
while len(q):
    x = q.popleft()
    if x == N:
        break
    next_t = data[x][0] + 1
    if x % 2 == 0 and data[x // 2][0] == -1:
        data[x // 2][0] = next_t
        data[x // 2][1] = x
        q.append(x // 2)
    if x > 0 and data[x - 1][0] == -1:
        data[x - 1][0] = next_t
        data[x - 1][1] = x
        q.append(x - 1)
    if x < 100000 and data[x + 1][0] == -1:
        data[x + 1][0] = next_t
        data[x + 1][1] = x
        q.append(x + 1)
s = N
result = str(data[N][0]) + '\n'
while True:
    result += str(s) + ' '
    if s == K:
        break
    s = data[s][1]
print(result[:-1])
