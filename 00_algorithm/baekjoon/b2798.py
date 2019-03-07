# https://www.acmicpc.net/problem/2798
# 블랙잭


from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0
for perm in combinations(cards, 3):
    temp = sum(perm)
    if result < temp <= M:
        result = temp
print(result)
