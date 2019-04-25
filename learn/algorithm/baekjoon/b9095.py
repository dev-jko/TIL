# https://www.acmicpc.net/problem/9095
# 1, 2, 3 더하기


dp = [1 for _ in range(11)]
dp[2] = 2
for i in range(3, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
for _ in range(int(input())):
    n = int(input())
    print(dp[n])
