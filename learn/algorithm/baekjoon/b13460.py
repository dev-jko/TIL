# https://www.acmicpc.net/problem/13460
# 구슬 탈출 2


def move(d, rx, ry, bx, by):
    rnx, rny = rx + dxy[d][0], ry + dxy[d][1]
    red_end = False
    while 0 <= rnx < N and 0 <= rny < M:
        if data[rnx][rny] == 'O':
            red_end = True
            break
        elif data[rnx][rny] == '#':
            rnx, rny = rnx - dxy[d][0], rny - dxy[d][1]
            break
        rnx, rny = rnx + dxy[d][0], rny + dxy[d][1]
    bnx, bny = bx + dxy[d][0], by + dxy[d][1]
    blue_end = False
    while 0 <= bnx < N and 0 <= bny < M:
        if data[bnx][bny] == 'O':
            blue_end = True
            break
        elif data[bnx][bny] == '#':
            bnx, bny = bnx - dxy[d][0], bny - dxy[d][1]
            break
        bnx, bny = bnx + dxy[d][0], bny + dxy[d][1]
    if red_end and not blue_end:
        return [True]
    elif blue_end:
        return [False]
    if d == 0 and rnx == bnx and rny == bny:
        if rx > bx:
            rx, bx = rnx + 1, bnx
        else:
            rx, bx = rnx, bnx + 1
    elif d == 1 and rnx == bnx and rny == bny:
        if rx > bx:
            rx, bx = rnx, bnx - 1
        else:
            rx, bx = rnx - 1, bnx
    elif d == 2 and rnx == bnx and rny == bny:
        if ry > by:
            ry, by = rny + 1, bny
        else:
            ry, by = rny, bny + 1
    elif d == 3 and rnx == bnx and rny == bny:
        if ry > by:
            ry, by = rny, bny - 1
        else:
            ry, by = rny - 1, bny
    else:
        rx, ry, bx, by = rnx, rny, bnx, bny
    return rx, ry, bx, by


def bt(k, d, rx, ry, bx, by):
    global result
    if k >= result or k >= 10:
        return
    else:
        for nd in dxy_set - {d}:
            moved = move(nd, rx, ry, bx, by)
            if len(moved) != 1:  # 안 끝날 때
                bt(k + 1, nd, moved[0], moved[1], moved[2], moved[3])
            elif moved[0]:  # 빨간 구슬 빼고 끝날때
                result = min(result, k + 1)
                return


dxy_set = {0, 1, 2, 3}
dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if data[i][j] == 'R':
            data[i][j] = '.'
            rx, ry = i, j
        if data[i][j] == 'B':
            data[i][j] = '.'
            bx, by = i, j
result = 0xffffffff
bt(0, -1, rx, ry, bx, by)
print(result if result != 0xffffffff else -1)
