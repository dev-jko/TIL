# 5249. [파이썬 S/W 문제해결 구현] 7일차 - 최소 신장 트리


from heapq import heappush, heappop

for T in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    G = [[-1] * (V + 1) for _ in range(V + 1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = G[n2][n1] = w
    q = []
    used = set()
    result = 0
    used.add(0)
    for i in range(V + 1):
        if G[0][i] >= 0:
            heappush(q, (G[0][i], i))
    while q:
        if len(used) >= V + 1:
            break
        w, n = heappop(q)
        if n not in used:
            result += w
            used.add(n)
            for i in range(V + 1):
                if G[n][i] >= 0 and i not in used:
                    heappush(q, (G[n][i], i))
    print('#{} {}'.format(T, result))

# def find_set(v):
#     if v != p[v]:
#         p[v] = find_set(p[v])
#     return p[v]
#
#
# for T in range(1, int(input()) + 1):
#     V, E = map(int, input().split())
#     p = [i for i in range(V + 1)]
#     edges = []
#     for _ in range(E):
#         n1, n2, w = map(int, input().split())
#         edges.append((w, n1, n2))
#     edges.sort(reverse=True)
#     result = 0
#     while V > 0:
#         w, n1, n2 = edges.pop()
#         pa, pb = find_set(n1), find_set(n2)
#         if pa != pb:
#             p[pb] = pa
#             V -= 1
#             result += w
#     print('#{} {}'.format(T, result))
