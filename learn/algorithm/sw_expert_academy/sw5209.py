# 5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용


def bt(data, k, selected, cost, result):
    if len(data) == k:
        result[0] = min(result[0], cost)
    else:
        for i in range(len(data)):
            if not selected[i] and cost + data[k][i] <= result[0]:
                selected[i] = True
                bt(data, k + 1, selected, cost + data[k][i], result)
                selected[i] = False


for T in range(1, int(input()) + 1):
    N = int(input())
    V = []
    for _ in range(N):
        V.append(list(map(int, input().split())))
    result = [999999]
    bt(V, 0, [False for _ in range(N)], 0, result)
    print(f'#{T} {result[0]}')
