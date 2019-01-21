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
            arrs90[j][N + 1 - i] = arrs[i][j]
    result = 0
    word = '0' + '1' * K + '0'
    for arr in arrs:
        string = ''.join(arr)
        result += string.count(word)
    for arr in arrs90:
        string = ''.join(arr)
        result += string.count(word)
    print(f'#{T} {result}')
