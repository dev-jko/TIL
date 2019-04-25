# https://www.acmicpc.net/problem/2250
#  트리의 높이와 너비


def inorder(v, level):
    if v == -1:
        return
    global idx
    lv[v] = level
    inorder(L[v], level + 1)
    col[v] = idx
    idx += 1
    inorder(R[v], level + 1)


N = int(input())
col = [-1 for _ in range(N + 1)]
lv = [-1 for _ in range(N + 1)]
P = [-1 for _ in range(N + 1)]
L = [-1 for _ in range(N + 1)]
R = [-1 for _ in range(N + 1)]
for _ in range(N):
    c, l, r = map(int, input().split())
    if l != -1:
        L[c] = l
        P[l] = c
    if r != -1:
        R[c] = r
        P[r] = c
idx = 1
root = 0
for i in range(1, N + 1):
    if P[i] == -1:
        root = i
        break
inorder(root, 1)
lv_len = max(lv) + 1
min_col = [9999 for _ in range(lv_len)]
max_col = [0 for _ in range(lv_len)]
width = [0 for _ in range(lv_len)]
for i in range(1, N + 1):
    if col[i] < min_col[lv[i]]:
        min_col[lv[i]] = col[i]
    if col[i] > max_col[lv[i]]:
        max_col[lv[i]] = col[i]
result = [-1, -1]
for i in range(1, lv_len):
    width[i] = max_col[i] - min_col[i] + 1
    if result[1] < width[i]:
        result[0], result[1] = i, width[i]
print(*result)
