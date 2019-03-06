# swea 5177.
# [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙


def insert(n):
    t.append(n)
    m = t.index(n)
    p = m // 2
    while m >= 1 and t[p] > t[m]:
        t[p], t[m] = t[m], t[p]
        m = p
        p //= 2


def get_ancestor(idx, s):
    if idx <= 1:
        return s
    temp = get_ancestor(idx // 2, s + t[idx // 2])
    return temp


for T in range(1, int(input()) + 1):
    N = int(input())
    data = list(map(int, input().split()))
    t = [0]
    for i in data:
        insert(i)
    print('#{} {}'.format(T, get_ancestor(len(t) - 1, 0)))
