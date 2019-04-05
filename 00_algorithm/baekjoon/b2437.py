# https://www.acmicpc.net/problem/2437
# 저울


N = int(input())
data = sorted(list(map(int, input().split())))
sums = data[0]
if sums > 1:
    print(1)
else:
    for i in range(1, N):
        if sums + 2 <= data[i]:
            break
        sums += data[i]
    print(sums + 1)
