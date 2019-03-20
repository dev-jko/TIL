# https://www.acmicpc.net/problem/14890
# 경사로


def check(arr):
    global result
    used = [False for _ in range(N)]
    leng = 1
    start = 1
    while start < N:
        if arr[start] == arr[start - 1]:
            leng += 1
        elif arr[start - 1] + 1 == arr[start]:
            if leng < L:
                return
            for j in range(start - L, start):
                used[j] = True
            leng = 1
        elif arr[start - 1] == arr[start] + 1:
            start -= 1
            break
        else:
            return
        start += 1
    end = N - 2
    leng = 1
    while end > -1:
        if arr[end] == arr[end + 1]:
            leng += 1
        elif arr[end + 1] + 1 == arr[end]:
            if leng < L:
                return
            for j in range(end + L, end, -1):
                if used[j]:
                    return
                used[j] = True
            leng = 1
        elif arr[end + 1] == arr[end] + 1:
            end += 1
            break
        else:
            return
        end -= 1
    if start >= end:
        result += 1


N, L = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(N)]

result = 0
for arr in data:
    check(arr)

t_d = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        t_d[j][N - i - 1] = data[i][j]
for arr in t_d:
    check(arr)

print(result)
