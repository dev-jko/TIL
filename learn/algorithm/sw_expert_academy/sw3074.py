# 3074. 입국심사


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    tk = sorted([int(input()) for _ in range(N)])
    start = 0
    end = tk[-1] * M + 1
    while start < end:
        check = True
        mid = (start + end) // 2
        result = 0
        for i in range(N):
            result += mid // tk[i]
            if result >= M:
                break
        else:
            check = False
        if check:
            end = mid
        else:
            start = mid + 1
    print('#{} {}'.format(T, start))
