# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3

from heapq import heappush, heappop

N, K = map(int, input().split())
q = []
data = [[9999999, False] for _ in range(100001)]
data[K][0] = 0
heappush(q, (0, K))
while len(q):
    t, x = heappop(q)
    if x == N:
        break
    data[x][1] = True
    if x % 2 == 0 and not data[x // 2][1] and t < data[x // 2][0]:
        data[x // 2][0] = t
        heappush(q, (t, x // 2))
    if 1 <= x and not data[x - 1][1] and t + 1 < data[x - 1][0]:
        data[x - 1][0] = t + 1
        heappush(q, (t + 1, x - 1))
    if x + 1 <= 100000 and not data[x + 1][1] and t + 1 < data[x + 1][0]:
        data[x + 1][0] = t + 1
        heappush(q, (t + 1, x + 1))
print(data[N][0])