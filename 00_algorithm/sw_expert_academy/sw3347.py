# 3347. 올림픽 종목 투표


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = sorted(list(map(int, input().split())), reverse=True)
    result = [0] * N
    idx = 0
    for i in range(N):
        while idx < M and B[idx] >= A[i]:
            result[i] += 1
            idx += 1
        if idx >= M:
            break
    print('#{} {}'.format(T, result.index(max(*result)) + 1))
