# https://www.acmicpc.net/problem/2477
# 참외밭

K = int(input())
d = []
o = []
for _ in range(6):
    a, b = map(int, input().split())
    d.append(b)
    o.append(a - 1)
small = big = 0
for i in range(len(o)):
    if o[i] == o[(i + 2) % 6] and o[(i + 1) % 6] == o[(i + 3) % 6]:
        small = d[(i + 1) % 6] * d[(i + 2) % 6]
        big = d[(i + 4) % 6] * d[(i + 5) % 6]
        break
print((big - small) * K)
