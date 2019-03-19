# https://www.acmicpc.net/problem/15685
# 드래곤 커브


def generate(n):
    temp_d = []
    temp_xy = []
    x, y = dragon[n][0][-1]
    for i in range(len(dragon[n][1]) - 1, -1, -1):
        nd = (dragon[n][1][i] + 1) % 4
        temp_d.append(nd)
        x += dxy[nd][0]
        y += dxy[nd][1]
        temp_xy.append((x, y))
    dragon[n][0] += temp_xy
    dragon[n][1] += temp_d


dxy = [[1, 0], [0, -1], [-1, 0], [0, 1]]
N = int(input())
dragon = [[[], []] for _ in range(N)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    dragon[i][1].append(d)
    dragon[i][0].append((x, y))
    dragon[i][0].append((x + dxy[d][0], y + dxy[d][1]))
    for j in range(g):
        generate(i)
total = set()
for dra in dragon:
    total |= set(dra[0])
result = 0
for x, y in total:
    if (x + 1, y) in total and (x, y + 1) in total and (x + 1, y + 1) in total:
        result += 1
print(result)
