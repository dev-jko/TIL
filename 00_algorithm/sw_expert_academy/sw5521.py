# 5521. 상원이의 생일파티


from collections import deque

q = deque()
for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    q.clear()
    q.append((1, 0))
    visited = [False] * (N + 1)
    visited[1] = True
    result = 0
    while q:
        m, cnt = q.popleft()
        if cnt < 2:
            for i in G[m]:
                if not visited[i]:
                    visited[i] = True
                    q.append((i, cnt + 1))
                    result += 1
    print('#{} {}'.format(T, result))
