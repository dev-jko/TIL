# https://www.acmicpc.net/problem/17071
# 숨바꼭질 5

# TODO 실패

from collections import deque

N, K = map(int, input().split())
q = deque()
visited = [-1 for _ in range(500001)]
visited2 = [-1 for _ in range(500001)]
visited[N] = 0
visited2[N] = 0

test = [-1 for _ in range(500001)]
test2 = [-1 for _ in range(500001)]
test[N] = N
test2[N] = N

q.append(N)
while len(q):
    x = q.popleft()
    next_t = visited[x] + 1
    if x * 2 <= 500000:
        if visited[x * 2] == -1:
            visited[x * 2] = next_t
            test[x * 2] = x
            q.append(x * 2)
        elif visited2[x * 2] == -1:
            visited2[x * 2] = next_t
            test2[x * 2] = x
            q.append(x * 2)
    if x > 0:
        if visited[x - 1] == -1:
            visited[x - 1] = next_t
            test[x - 1] = x
            q.append(x - 1)
        elif visited2[x - 1] == -1:
            visited2[x - 1] = next_t
            test2[x - 1] = x
            q.append(x - 1)
    if x < 500000:
        if visited[x + 1] == -1:
            visited[x + 1] = next_t
            q.append(x + 1)
            test[x + 1] = x
        elif visited2[x + 1] == -1:
            visited2[x + 1] = next_t
            q.append(x + 1)
            test2[x + 1] = x

result = 999999
t = 0

temp = False

while K <= 500000:
    if t == visited[K]:
        result = t
        break
    elif t > visited[K]:
        if (t - visited[K]) % 2 == 0:
            result = t
            break
    elif t == visited2[K]:
        result = t
        temp = True
        break
    elif t > visited2[K]:
        if (t - visited2[K]) % 2 == 0:
            temp = True
            result = t
            break
    t += 1
    K += t
print(result if result != 999999 else -1)

result = ''
s = K
print('---------')
while True:
    print(s, end=' - ')
    if s == N:
        break
    if temp:
        s = test2[s]
    else:
        s = test[s]


