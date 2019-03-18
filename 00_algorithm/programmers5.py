# https://www.acmicpc.net/problem/17071
# 백준 숨바꼭질 5

from collections import deque

N, K = map(int, input().split())
q = deque()
visited = [[-1, -1] for _ in range(500001)]  # 0홀수 1짝수
visited[N][1] = 0
q.append((N, 1))
while len(q):
    x, y = q.popleft()
    next_t = visited[x][y] + 1
    ny = 1 if next_t % 2 == 0 else 0
    if x * 2 <= 500000 and visited[x * 2][ny] == -1:
        visited[x * 2][ny] = next_t
        q.append((x * 2, ny))
    if x > 0 and visited[x - 1][ny] == -1:
        visited[x - 1][ny] = next_t
        q.append((x - 1, ny))
    if x < 500000 and visited[x + 1][ny] == -1:
        visited[x + 1][ny] = next_t
        q.append((x + 1, ny))
t = 0
temp = False
result = 9999999
while K <= 500000:
    if t == visited[K][0]:
        result = min(result, t)
    if t > visited[K][0]:
        if visited[K][0] != -1 and (t - visited[K][0]) % 2 == 0:
            result = min(result, t)
    if t == visited[K][1]:
        result = min(result, t)
        temp = True
    if t > visited[K][1]:
        if visited[K][1] != -1 and (t - visited[K][1]) % 2 == 0:
            temp = True
            result = min(result, t)
    t += 1
    K += t
print(result if result != 9999999 else -1)
