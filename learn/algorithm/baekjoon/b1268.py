# https://www.acmicpc.net/problem/1268
# 임시 반장 정하기


N = int(input())
data = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(N)]
c = [[set() for _ in range(10)] for _ in range(5)]
for i in range(N):
    for j in range(5):
        c[j][data[i][j]].add(i)
cnt = [0] * N
for i in range(N):
    temp = set()
    for j in range(5):
        temp |= c[j][data[i][j]]
    cnt[i] = len(temp)
print(cnt.index(max(cnt)) + 1)
