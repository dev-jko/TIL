# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기


def find_set(v):
    if p[v] != v:
        p[v] = find_set(p[v])
    return p[v]


def union(a, b):
    pa, pb = find_set(a), find_set(b)
    if pa != pb:
        p[pb] = pa


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    p = [i for i in range(N + 1)]
    for i in range(0, M * 2, 2):
        union(data[i], data[i + 1])
    for i in range(1, N + 1):
        find_set(i)
    print('#{} {}'.format(T, len(set(p)) - 1))
