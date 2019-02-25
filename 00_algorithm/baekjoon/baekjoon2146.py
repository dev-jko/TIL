# TODO  실패

def bind_ground(m, n, group):
    global data, N
    data[m][n] = group
    if m > 0 and data[m - 1][n] == 1:
        bind_ground(m - 1, n, group)
    if m < N - 1 and data[m + 1][n] == 1:
        bind_ground(m + 1, n, group)
    if n > 0 and data[m][n - 1] == 1:
        bind_ground(m, n - 1, group)
    if n < N - 1 and data[m][n + 1] == 1:
        bind_ground(m, n + 1, group)


def check(min_len, m, n):
    global data, N
    if data[m][n] == 0:
        return
    for i in range(N):
        for j in range(N):
            if data[i][j] not in [data[m][n], 0]:
                length = abs(i - m) + abs(j - n) - 1
                min_len[0] = min(min_len[0], length)


N = int(input())
data = []
for _ in range(N):
    data.append([int(i) for i in sys.stdin.readline()[:-1].split()])
    # data.append(list(map(int, input().split())))

print(data)

group = 2
for i in range(N):
    for j in range(N):
        if data[i][j] == 1:
            bind_ground(i, j, group)
            group += 1
result = [100000]
d = [[0, -1], [0, 1], [-1, 0], [1, 0]]
for i in range(N):
    for j in range(N):
        check(result, i, j)
print(result[0])

# def bt(min_len, m, n, group, cnt):
#     global data, N, d
#     for x, y in d:
#         if 0 <= m + x < N and 0 <= n + y < N and data[m + x][n + y] == group:
#             break
#     else:
#         return
#     if data[m][n] not in [group, 0, 1]:
#         min_len[0] = min(min_len[0], cnt)
#         # for arr in data:
#         #     print(arr)
#         # print(group, cnt, result[0])
#     elif min_len[0] >= cnt + 1:
#         temp = data[m][n]
#         data[m][n] = group
#         for x, y in d:
#             if 0 <= m + x < N and 0 <= n + y < N and data[m + x][n + y] != group:
#                 bt(min_len, m + x, n + y, group, cnt + 1)
#         data[m][n] = temp
