# https://www.acmicpc.net/problem/2304
# 창고 다각형


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data.sort()
result = 0
left = 0
right = N - 1
for i in range(1, N):
    if data[left][1] < data[i][1]:
        result += (data[i][0] - data[left][0]) * data[left][1]
        left = i
for i in range(N - 1, -1, -1):
    if data[right][1] < data[i][1]:
        result += (data[right][0] - data[i][0]) * data[right][1]
        right = i
if left == right:
    result += data[left][1]
elif left < right:
    result += (data[right][0] - data[left][0] + 1) * (min(data[right][1], data[left][1])) + abs(
        data[right][1] - data[left][1])
print(result)
