for T in range(1, int(input()) + 1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input())))
    result = 0
    start, end = N // 2, N // 2 + 1
    for i in range(N):
        for j in range(start, end):
            result += data[i][j]
        if i < N // 2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{T} {result}')
