from collections import deque

q = deque()
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    q.clear()
    inputs = list(map(int, input().split()))
    for n in inputs:
        q.append(n)
    for _ in range(M):
        q.append(q.popleft())
    print('#{} {}'.format(T, q.popleft()))
