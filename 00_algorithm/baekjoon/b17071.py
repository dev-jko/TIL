# https://www.acmicpc.net/problem/17071
# 숨바꼭질 5

from collections import deque

N, K = map(int, input().split())
data = [[-1, -1] for _ in range(500001)]  # 0짝수 1홀수
data[N][0] = 0
q = deque()
q.append((N, 0))
while q:
    x, y = q.popleft()
    for nx in x * 2, x + 1, x - 1:
        ny = 1 - y
        if 0 <= nx <= 500000 and data[nx][ny] == -1:
            data[nx][ny] = data[x][y] + 1
            q.append((nx, ny))
t = 0
result = 9999999
while K <= 500000:
    y = t % 2
    if data[K][y] != -1 and data[K][y] <= t:
        result = min(result, t)
    t += 1
    K += t
print(result if result != 9999999 else -1)
