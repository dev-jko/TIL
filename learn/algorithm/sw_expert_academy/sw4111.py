# 4111. 무선 단속 카메라


for T in range(1, int(input()) + 1):
    input()
    K = int(input())
    data = sorted(list(set(map(int, input().split()))))
    N = len(data)
    result = 0
    if N > K:
        d = []
        for i in range(1, N):
            d.append(data[i] - data[i - 1])
        d.sort()
        temp = N - K
        for i in range(temp):
            result += d[i]
    print('#{} {}'.format(T, result))
