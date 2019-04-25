# https://www.acmicpc.net/problem/15686
# 치킨 배달

from itertools import combinations


def get_d(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
chik = []
home = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 2:
            chik.append((i, j))
        elif data[i][j] == 1:
            home.append((i, j))
d_arr = [[get_d(*home[i], *chik[j]) for j in range(len(chik))] for i in range(len(home))]
result = 0xffffff
for combi in combinations([i for i in range(len(chik))], M):
    temp = 0
    for d in d_arr:
        tt = 0xffffff
        for i in combi:
            tt = min(tt, d[i])
        temp += tt
    result = min(result, temp)
print(result)
