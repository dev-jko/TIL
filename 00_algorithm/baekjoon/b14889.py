# https://www.acmicpc.net/problem/14889
# 스타트와 링크


from itertools import combinations

N = int(input())
S = [[i for i in map(int, input().split())] for _ in range(N)]
result = 0xffffff
member = {i for i in range(N)}
for combi in combinations(range(N), N // 2):
    temp = 0
    for x, y in combinations(combi, 2):
        temp += S[x][y] + S[y][x]
    for x, y in combinations(member - set(combi), 2):
        temp -= S[x][y] + S[y][x]
    result = min(result, abs(temp))
    if result == 0:
        break
print(result)
