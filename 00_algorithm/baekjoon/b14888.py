# https://www.acmicpc.net/problem/14888
# 연산자 끼워넣기


def dfs(k, result):
    if k == N:
        global max_result, min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    else:
        for i in range(4):
            if inputs[i] > 0:
                inputs[i] -= 1
                temp = result
                if i == 0:
                    temp += numbers[k + 1]
                elif i == 1:
                    temp -= numbers[k + 1]
                elif i == 2:
                    temp *= numbers[k + 1]
                else:
                    if temp < 0:
                        temp = -temp // numbers[k + 1] * -1
                    else:
                        temp //= numbers[k + 1]
                dfs(k + 1, temp)
                inputs[i] += 1


N = int(input()) - 1
numbers = list(map(int, input().split()))
inputs = list(map(int, input().split()))
operators = [-1 for _ in range(N)]
max_result = -0xfffffffff
min_result = 0xfffffffff
dfs(0, numbers[0])
print('{}\n{}'.format(max_result, min_result))


# from itertools import permutations
#
# N = int(input())
# numbers = list(map(int, input().split()))
# inputs = list(map(int, input().split()))
# operators = []
# for i in range(4):
#     operators += [i for _ in range(inputs[i])]
# max_result = -0xfffffffff
# min_result = 0xfffffffff
# for perm in set(permutations(operators)):
#     temp = numbers[0]
#     for i in range(N - 1):
#         if perm[i] == 0:
#             temp += numbers[i + 1]
#         elif perm[i] == 1:
#             temp -= numbers[i + 1]
#         elif perm[i] == 2:
#             temp *= numbers[i + 1]
#         else:
#             if temp < 0:
#                 temp = -temp // numbers[i + 1] * -1
#             else:
#                 temp //= numbers[i + 1]
#     max_result = max(max_result, temp)
#     min_result = min(min_result, temp)
# print('{}\n{}'.format(max_result, min_result))
