# https://www.acmicpc.net/problem/1002
# 터렛


def calculate():
    pass


for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
            continue
        else:
            print(0)
            continue
    b1, s1 = x1, x2
    if b1 < s1:
        b1, s1 = s1, b1
    b2, s2 = y1, y2
    if b2 < s2:
        b2, s2 = s2, b2
    result = 0
    for i in range(s1, b1 + 1):
        for j in range(s2, s2 + 1):
            d1 = abs()

    print(result)
