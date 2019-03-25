# https://www.acmicpc.net/problem/2167
# 2차원 배열의 합

N, M = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]
K = int(input())
ijxy = [list(map(int, input().split())) for _ in range(K)]
for i in range(1, N):
    data[i][0] += data[i - 1][0]
for i in range(1, M):
    data[0][i] += data[0][i - 1]
for i in range(1, N):
    for j in range(1, M):
        data[i][j] += data[i][j - 1] + data[i - 1][j] - data[i - 1][j - 1]
for i, j, x, y in ijxy:
    i -= 1
    j -= 1
    x -= 1
    y -= 1
    result = data[x][y]
    if i > 0:
        result -= data[i - 1][y]
    if j > 0:
        result -= data[x][j - 1]
    if i > 0 and j > 0:
        result += data[i - 1][j - 1]
    print(result)
