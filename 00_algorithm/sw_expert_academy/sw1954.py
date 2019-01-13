d = ((1, 0), (0, -1), (-1, 0), (0, 1))
for T in range(1, int(input()) + 1):
    N = int(input())
    arrs = [[i for i in range(1, N + 1)] for i in range(N)]
    d_i = j = 0
    k = c = N - 1
    i = N + 1
    while i <= N * N:
        for _ in range(2):
            for _ in range(c):
                j += d[d_i][0]
                k += d[d_i][1]
                arrs[j][k] = i
                i += 1
            d_i = (d_i + 1) if d_i < 3 else 0
        c -= 1

    print(f'#{T}')
    for arr in arrs:
        print(*arr)
