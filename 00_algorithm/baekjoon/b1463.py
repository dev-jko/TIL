# https://www.acmicpc.net/problem/1463
# 1로 만들기


def dfs(num, cnt):
    if num == 1:
        memo[1] = min(memo[1], cnt)
        return
    if cnt >= memo[1]:
        return
    if num % 3 == 0 and (memo[num // 3] == -1 or memo[num // 3] > cnt + 1):
        memo[num // 3] = cnt + 1
        dfs(num // 3, cnt + 1)
    if num % 2 == 0 and (memo[num // 2] == -1 or memo[num // 2] > cnt + 1):
        memo[num // 2] = cnt + 1
        dfs(num // 2, cnt + 1)
    if memo[num - 1] == -1 or memo[num - 1] > cnt + 1:
        memo[num - 1] = cnt + 1
        dfs(num - 1, cnt + 1)


X = int(input())
memo = [-1 for _ in range(X + 1)]
memo[1] = 0xffffffff
dfs(X, 0)
print(memo[1])





# def dfs(num, cnt):
#     if num == 1:
#         global result
#         result = min(result, cnt)
#         return
#     if cnt >= result:
#         return
#     if num % 3 == 0:
#         dfs(num // 3, cnt + 1)
#     if num % 2 == 0:
#         dfs(num // 2, cnt + 1)
#     dfs(num - 1, cnt + 1)
#
# X = int(input())
# result = 0xffffffff
# dfs(X, 0)
# print(result)






# X = int(input())
# dp = [0xffffff for _ in range(X + 1)]
# dp[0] = dp[1] = 0
# for i in range(1, X + 1):
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i // 3] + 1)
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i // 2] + 1)
#     dp[i] = min(dp[i], dp[i - 1] + 1)
# print(dp[X])
