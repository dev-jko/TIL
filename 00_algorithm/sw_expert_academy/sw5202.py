# 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크


for T in range(1, int(input()) + 1):
    N = int(input())
    se = []
    for _ in range(N):
        se.append(list(map(int, input().split())))
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if se[j][1] > se[j + 1][1]:
                se[j], se[j + 1] = se[j + 1], se[j]
    result = 0
    end = 0
    for value in se:
        if value[0] >= end:
            end = value[1]
            result += 1
    print(f'#{T} {result}')
