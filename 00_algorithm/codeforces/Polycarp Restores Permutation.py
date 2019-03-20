# https://codeforces.com/problemset/problem/1141/C
# C. Polycarp Restores Permutation

n = int(input())
data = list(map(int, input().split()))
result = [1]
min_p = 1
for i in range(1, n):
    next_p = result[i - 1] + data[i - 1]
    min_p = min(min_p, next_p)
    result.append(next_p)
if min_p != 1:
    d = 1 - min_p
    for i in range(n):
        result[i] += d
print(' '.join(map(str, result)) if set(result) == set(range(1, n + 1)) else -1)
