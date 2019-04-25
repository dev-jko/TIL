# https://www.acmicpc.net/problem/2578
# 빙고


def check_bingo():
    cnt = 0
    cr1 = cr2 = True
    for i in range(5):
        r = True
        c = True
        for j in range(5):
            r &= used[i][j]
            c &= used[j][i]
        cr1 &= used[i][i]
        cr2 &= used[4 - i][i]
        if r:
            cnt += 1
        if c:
            cnt += 1
    if cr1:
        cnt += 1
    if cr2:
        cnt += 1
    return cnt


data = []
for _ in range(5):
    data.append(list(map(int, input().split())))
calls = []
for _ in range(5):
    calls.append(list(map(int, input().split())))
used = [[False for _ in range(5)] for _ in range(5)]
cnt = 0
check = False
for k in range(5):
    for l in range(5):
        cnt += 1
        for i in range(5):
            for j in range(5):
                if data[i][j] == calls[k][l]:
                    used[i][j] = True
        if check_bingo() >= 3:
            check = True
            break
    if check:
        break
print(cnt)
