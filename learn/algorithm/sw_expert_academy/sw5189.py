# 5189. [파이썬 S/W 문제해결 구현] 2일차 - 전자카트


def perm(n, k):
    if k == n:
        global result
        temp = e[0][a[0]] + e[a[-1]][0]
        for i in range(len(a) - 1):
            temp += e[a[i]][a[i + 1]]
        result = min(result, temp)
    else:
        for i in range(k, n):
            a[k], a[i] = a[i], a[k]
            perm(n, k + 1)
            a[k], a[i] = a[i], a[k]


for T in range(1, int(input()) + 1):
    N = int(input())
    e = []
    for _ in range(N):
        e.append(list(map(int, input().split())))
    result = 999999
    a = [i for i in range(1, N)]
    perm(N - 1, 0)
    print(f'#{T} {result}')
