for T in range(1, int(input()) + 1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{T} {min(P * W, Q + (0 if W <= R else ((W - R) * S)))}')

# for T in range(1, int(input()) + 1):
#     P, Q, R, S, W = map(int, input().split())
#     result = min(P * W, Q + (0 if W <= R else ((W - R) * S)))
#     print(f'#{T} {result}')
