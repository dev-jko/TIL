def bt(k, n, col, sum_num, table, result):
    if k == n:
        result[0] = min(result[0], sum_num)
    else:
        for i in range(n):
            if not col[i] and table[k][i] + sum_num < result[0]:
                col[i] = True
                bt(k + 1, n, col, table[k][i] + sum_num, table, result)
                col[i] = False


for T in range(1, int(input()) + 1):
    N = int(input())
    table = []
    for _ in range(N):
        table.append(list(map(int, input().split())))
    result = [9999999]
    bt(0, N, [False for _ in range(N)], 0, table, result)
    print(f'#{T} {result[0]}')
