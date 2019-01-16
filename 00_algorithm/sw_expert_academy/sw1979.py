# TODO 풀다 맘

for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arrs = [['0' for _ in range(N + 2)]]
    for i in range(N):
        arrs.append(input().split())
        arrs[i + 1].insert(0, '0')
        arrs[i + 1].append('0')
    arrs.append(['0' for _ in range(N + 2)])
    arrs90 = [['0' for _ in range(N + 2)] for _ in range(N + 2)]
    for i in range(N + 2):
        for j in range(N + 2):
            arrs90[j][N + 2 - i] = arrs[i][j]

    print(arrs90)

    result = 0
    word = '0' + '1' * K + '0'
    for arr in arrs:
        string = ''.join(arr)
        if word in string:
            result += 1

    print(arrs)

    print(f'#{T} {result}')
