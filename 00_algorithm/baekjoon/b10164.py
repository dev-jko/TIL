# https://www.acmicpc.net/problem/10164
# 격자상의 경로


def get_route(sx, sy, ex, ey):
    for i in range(sx, ex + 1):
        for j in range(sy, ey + 1):
            if sx == i and sy == j:
                continue
            data[i][j] = data[i - 1][j] + data[i][j - 1]


N, M, K = map(int, input().split())
data = [[0] * (M + 1) for _ in range(N + 1)]
data[1][1] = 1
if K != 0:
    if K % M == 0:
        mx, my = K // M, M
    else:
        mx, my = K // M + 1, K % M
    get_route(1, 1, mx, my)
    get_route(mx, my, N, M)
else:
    get_route(1, 1, N, M)
print(data[-1][-1])
