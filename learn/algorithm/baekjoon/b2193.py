# https://www.acmicpc.net/problem/2193
# 이친수

N = int(input())
dp = [0, 1, 1, 2, 3]
for i in range(5, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[N])
