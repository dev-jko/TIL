# https://www.acmicpc.net/problem/2294
# 동전 2

n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))
coins = list(coins)
dp = [0 for _ in range(k + 1)]
for i in range(1, k + 1):
    temp = 0xffffffff
    for coin in coins:
        if i >= coin and dp[i - coin] != -1:
            temp = min(temp, dp[i - coin] + 1)
    dp[i] = temp if temp != 0xffffffff else -1
print(dp[k])
