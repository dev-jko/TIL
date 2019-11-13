from collections import deque
import sys
input = sys.stdin.readline
N, M, T = map(int, input().split())
pan = [deque(map(int, input().split())) for _ in range(N)]
cmd = [list(map(int, input().split())) for _ in range(T)]

for x, d, k in cmd:
    for i in range(x - 1, N, x):
        if d == 0:
            pan[i].rotate(k)
        else:
            pan[i].rotate(-k)

    d = set()
    for i in range(N):
        for j in range(M):
            if pan[i][j] <= 0:
                continue
            if pan[i][j] == pan[i][j - 1]:
                d.add((i, j))
                d.add((i, j - 1))
            if i > 0 and pan[i][j] == pan[i - 1][j]:
                d.add((i, j))
                d.add((i - 1, j))
    if len(d) > 0:
        for i, j in d:
            pan[i][j] = 0
    else:
        m, c = 0, 0
        for a in pan:
            for n in a:
                if n > 0:
                    m += n
                    c += 1
        if c == 0:
            continue
        m /= c
        for i in range(N):
            for j in range(M):
                if 0 < pan[i][j] < m:
                    pan[i][j] += 1
                elif pan[i][j] > m:
                    pan[i][j] -= 1
for a in pan:
    print(a)

print(sum(sum(a) for a in pan))

# 2 2 2
# 1 2
# 3 4
# 2 0 1
# 2 1 1
