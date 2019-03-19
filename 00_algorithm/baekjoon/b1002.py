# https://www.acmicpc.net/problem/1002
# 터렛

for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(-1 if r1 == r2 else 0)
        continue
    result = 0
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    if d > r1 + r2 or d + r2 < r1 or d + r1 < r2:
        result = 0
    elif d == r1 + r2 or d + r1 == r2 or d + r2 == r1:
        result = 1
    else:
        result = 2
    print(result)
