# for T in range(1, int(input()) + 1):
#     N, M = map(int, input().split())
#     arrs = []
#     for _ in range(N):
#         arrs.append(list(map(int, input().split())))
#     result = 0
#     for i in range(N - M + 1):
#         for j in range(N - M + 1):
#             temp = sum( sum(arrs[x][j:j + M]) for x in range(i, i + M))
#             result = max(result, temp)
#
#     print(f'#{T} {result}')



for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    result = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            temp = 0
            for k in range(i, i + M):
                for l in range(j, j + M):
                    temp += data[k][l]
            result = max(result, temp)
    print('#{} {}'.format(T, result))