for T in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    arrs = []
    for i in range(N):
        arrs.append(input().split())
    arrs90 = [['' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arrs90[j][N - 1 - i] = arrs[i][j]
    result = 0
    word = '0' + '1' * K + '0'
    for arr in arrs:
        string = '0' + ''.join(arr) + '0'
        for i in range(N):
            temp = string[i:i+len(word)]
            if string[i:i+len(word)] == word:
                result += 1
    for arr in arrs90:
        string = '0' + ''.join(arr) + '0'
        for i in range(N):
            temp = string[i:i+len(word)]
            if string[i:i+len(word)] == word:
                result += 1
    print(f'#{T} {result}')
