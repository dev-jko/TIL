# https://www.acmicpc.net/problem/2591
# 숫자카드


data = list(map(int, input()))
N = len(data)
dp = [[0, 0] for _ in range(N)]
dp[0][0] = 1
for i in range(1, N):
    if 1 <= data[i - 1] <= 3 and 10 <= data[i - 1] * 10 + data[i] <= 34:
        dp[i][1] += dp[i - 1][0]
    if data[i] != 0:
        dp[i][0] += dp[i - 1][0] + dp[i - 1][1]
print(dp[-1][0] + dp[-1][1])

