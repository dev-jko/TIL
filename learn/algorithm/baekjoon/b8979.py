# https://www.acmicpc.net/problem/8979
# 올림픽


def sort(k):
    for i in range(N - 1, 0, -1):
        for j in range(i):
            if data[j][k] < data[j + 1][k]:
                data[j], data[j + 1] = data[j + 1], data[j]


N, K = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
    if data[-1][0] == K:
        target = data[-1]
sort(3)
sort(2)
sort(1)
for i in range(N):
    if data[i][1] == target[1] and data[i][2] == target[2] and data[i][3] == target[3]:
        print(i + 1)
        break
