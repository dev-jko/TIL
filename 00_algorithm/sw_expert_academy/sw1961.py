for T in range(1, int(input()) + 1):
    N = int(input())
    arrs = []
    for i in range(N):
        arrs.append(input().split())

    arrs90 = [[0 for _ in range(N)] for _ in range(N)]
    arrs180 = [[0 for _ in range(N)] for _ in range(N)]
    arrs270 = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrs90[j][N - i - 1] = arrs[i][j]
        arrs180[N - i - 1] = reversed(arrs[i])
        arrs270[N - i - 1] = reversed(arrs90[i])

    result = ''
    for i in range(N):
        result += ''.join(arrs90[i]) + ' '
        result += ''.join(arrs180[i]) + ' '
        result += ''.join(arrs270[i]) + '\n'
    print(f'#{T}\n{result[:-1]}')
