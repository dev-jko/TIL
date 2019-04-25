# 5251. [파이썬 S/W 문제해결 구현] 7일차 - 최소 이동 거리


from heapq import heappush, heappop

for T in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s].append((e, w))
    visited = [-1] * (N + 1)
    q = []
    heappush(q, (0, 0))
    while q:
        w, v = heappop(q)
        if visited[v] == -1 or visited[v] > w:
            visited[v] = w
            for nv, nw in G[v]:
                heappush(q, (w + nw, nv))
    print('#{} {}'.format(T, visited[N]))
