for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    min_sum = 1000001
    max_sum = 0
    for i in range(N - M + 1):
        t = 0
        for j in range(M):
            t += arr[i + j]
        min_sum = t if t < min_sum else min_sum
        max_sum = t if t > max_sum else max_sum
    print(f'#{T} {max_sum - min_sum}')
