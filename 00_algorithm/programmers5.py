from collections import deque

q = deque()
C, B = map(int, input().strip().split())
C_p = [C]
a = 1
p = C
while p < 200000:
    p += a
    C_p.append(p)
    a += 1
if C_p[-1] > 200000:
    C_p.pop()
q.append((B, 0))
result = -1
visited = [False for _ in range(200001)]
visited[B] = True
while len(q):
    x, t = q.popleft()
    if t >= len(C_p):
        continue
    if x == C_p[t]:
        result = t
        break
    else:
        nx = x * 2
        if nx <= 200000 and not visited[nx]:
            visited[nx] = True
            q.append((nx, t + 1))
        nx = x - 1
        if 0 < nx <= 200000 and not visited[nx]:
            visited[nx] = True
            q.append((nx, t + 1))
        nx = x + 1
        if nx <= 200000 and not visited[nx]:
            visited[nx] = True
            q.append((nx, t + 1))
print(result)
