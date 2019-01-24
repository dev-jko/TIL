for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    short_nums = list(map(int, input().split()))
    long_nums = list(map(int, input().split()))
    if N > M:
        N, M, short_nums, long_nums = M, N, long_nums, short_nums
    result = -99999999999
    for i in range(M - N + 1):
        temp = 0
        for j in range(N):
            temp += short_nums[j] * long_nums[i + j]
        result = max(result, temp)
    print(f'#{T} {result}')
