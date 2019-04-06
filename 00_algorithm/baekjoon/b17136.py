# https://www.acmicpc.net/problem/17136
# 색종이 붙이기


def dfs(k, r):
    global result
    if r <= 0:
        result = min(result, k)
    if k >= 25:
        return
    else:
        if k + 1 >= result:
            return
        for i in range(H):
            for j in range(W):
                if data[i][j] == 1:
                    for c in range(5, 0, -1):
                        if check(i, j, c):
                            if used[c] > 0:
                                used[c] -= 1
                                change(i, j, c, 0)
                                dfs(k + 1, r - (c * c))
                                used[c] += 1
                                change(i, j, c, 1)
                    else:
                        return


def change(x, y, c, v):
    for i in range(x, x + c):
        for j in range(y, y + c):
            data[i][j] = v


def check(x, y, c):
    for i in range(x, x + c):
        for j in range(y, y + c):
            if i >= H or j >= W or data[i][j] != 1:
                return False
    return True


data = []
total = 0
for _ in range(10):
    t = list(map(int, input().split()))
    s = sum(t)
    if s != 0:
        total += s
        data.append(t)
H = len(data)
i = 0
idx = 10
while i < idx:
    tt = 0
    for j in range(H):
        tt += data[j][i]
    if tt == 0:
        for j in range(H):
            data[j].pop(i)
        idx -= 1
    else:
        i += 1
W = len(data[0]) if len(data) else 0
used = [5] * 6
result = 26
dfs(0, total)
print(result if result != 26 else -1)
