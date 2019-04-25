# https://codeforces.com/problemset/problem/4/A
# 4A - Watermelon

N = int(input())
for i in range(2, N, 2):
    if (N - i) % 2 == 0:
        print('YES')
        exit(0)
print('NO')
