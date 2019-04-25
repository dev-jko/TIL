# https://www.acmicpc.net/problem/2643
# 색종이 올려 놓기


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    if data[i][0] < data[i][1]:
        data[i][0], data[i][1] = data[i][1], data[i][0]
data.sort()
result = [0] * N
result[0] = 1
for i in range(1, N):
    result[i] = max(result[i - 1][0], result[i - 1][1])
    temp = 0
    for j in range(i):
        if data[i][0] >= data[j][0] and data[i][1] >= data[j][1]:
            temp = max(temp, result[j][1])
    result[i][1] = temp + 1
print(max(result))
