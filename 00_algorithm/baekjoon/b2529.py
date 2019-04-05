# https://www.acmicpc.net/problem/2529
# 부등호


k = int(input())
data = input().split()
max_result = [0] * (k + 1)
min_result = [0] * (k + 1)
idx = 0
cnt = 0
used = 9
while idx <= k:
    if idx < k and data[idx] == '<':
        cnt += 1
        idx += 1
    else:
        for i in range(cnt + 1):
            max_result[idx - i] = used
            used -= 1
        idx += 1
        cnt = 0
idx = 0
cnt = 0
used = 0
while idx <= k:
    if idx < k and data[idx] == '>':
        cnt += 1
        idx += 1
    else:
        for i in range(cnt + 1):
            min_result[idx - i] = used
            used += 1
        idx += 1
        cnt = 0
print(''.join(map(str, max_result)))
print(''.join(map(str, min_result)))
