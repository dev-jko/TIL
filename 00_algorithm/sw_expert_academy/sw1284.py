for T in range(1, int(input()) + 1):
    P, Q, R, S, W = map(int, input().split())
    result = P * W
    temp = Q + (0 if W <= R else ((W - R) * S))
    result = min(result, temp)
    print(f'#{T} {result}')
