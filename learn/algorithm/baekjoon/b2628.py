# https://www.acmicpc.net/problem/2628
# 종이자르기


x, y = map(int, input().split())
N = int(input())
cut_x = [0, x]
cut_y = [0, y]
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0:
        cut_y.append(b)
    else:
        cut_x.append(b)
cut_x.sort()
cut_y.sort()
x_l = []
y_l = []
for i in range(len(cut_x) - 1):
    x_l.append(cut_x[i + 1] - cut_x[i])
for i in range(len(cut_y) - 1):
    y_l.append(cut_y[i + 1] - cut_y[i])
x_l.sort()
y_l.sort()
result = x_l[-1] * y_l[-1]
print(result)
