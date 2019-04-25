# 5247. [파이썬 S/W 문제해결 구현] 6일차 - 연산


from collections import deque

q = deque()
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    q.clear()
    q.append((N, 0))
    visited = [False] * 1000001
    visited[N] = True
    while q:
        n, cnt = q.popleft()
        if n == M:
            print('#{} {}'.format(T, cnt))
            break
        if n + 1 <= 1000000 and not visited[n + 1]:
            visited[n + 1] = True
            q.append((n + 1, cnt + 1))
        if n > 1 and not visited[n - 1]:
            visited[n - 1] = True
            q.append((n - 1, cnt + 1))
        if n * 2 <= 1000000 and not visited[n * 2]:
            visited[n * 2] = True
            q.append((n * 2, cnt + 1))
        if n > 10 and not visited[n - 10]:
            visited[n - 10] = True
            q.append((n - 10, cnt + 1))
