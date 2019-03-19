# https://www.acmicpc.net/problem/1004
# 어린 왕자


def is_inside(x, y, cx, cy, r):
    return False if ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5 > r else True


for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(int(input()))]
    result = 0
    for arr in data:
        if is_inside(x1, y1, *arr) ^ is_inside(x2, y2, *arr):
            result += 1
    print(result)
