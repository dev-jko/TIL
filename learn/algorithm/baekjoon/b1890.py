# https://www.acmicpc.net/problem/1890
# 점프

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if data[i][j] <= 0:
            continue
        if j + data[i][j] < N:
            dp[i][j + data[i][j]] += dp[i][j]
        if i + data[i][j] < N:
            dp[i + data[i][j]][j] += dp[i][j]
print(dp[-1][-1])
