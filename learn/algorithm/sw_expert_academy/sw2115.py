# swea 2115.
# [모의 SW 역량테스트] 벌꿀채취


def dfs(row, start, k, n, c, check):
    global set_result, C
    if k == n:
        if c > C:
            return
        t_p = 0
        for i in range(n):
            if check[i]:
                t_p += SQUARE[row][start + i]
        if t_p > set_result:
            set_result = t_p
        return
    else:
        dfs(row, start, k + 1, n, c, check)
        if c + data[row][start + k] <= C:
            check[k] = 1
            dfs(row, start, k + 1, n, c + data[row][start + k], check)
            check[k] = 0


for T in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    SQUARE = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            SQUARE[i][j] = data[i][j] ** 2
    profit = []
    for i in range(N):
        for j in range(N - M + 1):
            set_result = 0
            dfs(i, j, 0, M, 0, [0 for _ in range(M)])
            temp = [set_result, set({})]
            for k in range(j, j + M + 1):
                temp[1].add((i, k))
            profit.append(temp)
    result = 0
    for i in range(len(profit)):
        for j in range(len(profit)):
            if profit[i][0] + profit[j][0] > result and len(profit[i][1] & profit[j][1]) == 0:
                result = profit[i][0] + profit[j][0]
    print('#{} {}'.format(T, result))
