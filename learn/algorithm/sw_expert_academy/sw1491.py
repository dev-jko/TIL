# 1491. 원재의 벽 꾸미기


for T in range(1, int(input()) + 1):
    N, A, B = map(int, input().split())
    result = 0xffffffff
    for i in range(1, N + 1):
        t = B * (N - i * i)
        for j in range(i, 0, -1):
            temp = A * abs(i - j) + B * (N - i * j)
            if i * j > N or temp > t:
                break
            elif i * j <= N:
                result = min(result, temp)
        t = A + B * (N - i * (i + 1))
        for j in range(i + 1, N + 1):
            temp = A * abs(i - j) + B * (N - i * j)
            if i * j > N or temp > t:
                break
            elif i * j <= N:
                result = min(result, temp)
    print('#{} {}'.format(T, result))
