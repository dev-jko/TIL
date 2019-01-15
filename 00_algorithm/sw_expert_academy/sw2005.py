for T in range(1, int(input()) + 1):
    N = int(input())
    arrs = [[0 for i in range(N)] for i in range(N)]

    for i in range(N):
        arrs[i][0] = 1
        for j in range(1, N):
            arrs[i][j] = arrs[i - 1][j - 1] + arrs[i - 1][j]
    result = f'#{T}\n'
    for i in range(N):
        for j in range(i + 1):
            result += f'{arrs[i][j]} '
        result += '\n'
    print(result)
