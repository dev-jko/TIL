# swea 5178.
# [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합


def postorder(v):
    if v >= len(t):
        return 0
    if t[v] == -1:
        t[v] = postorder(v * 2) + postorder(v * 2 + 1)
    return t[v]


for T in range(1, int(input()) + 1):
    N, M, L = map(int, input().split())
    t = [-1 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        t[a] = b
    postorder(1)
    print('#{} {}'.format(T, t[L]))
