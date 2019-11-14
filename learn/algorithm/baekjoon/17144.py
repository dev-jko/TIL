def spread():
    global A, machine, R, C
    new_A = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if A[i][j] <= 0:
                continue
            t = A[i][j] // 5
            t_cnt = 0
            for dr, dc in dd:
                nr, nc = i + dr, j + dc
                if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                    t_cnt += 1
                    new_A[nr][nc] += t
            new_A[i][j] += A[i][j] - t * t_cnt
    for r in machine:
        new_A[r][0] = -1
    A = new_A


def wind():
    global A, machine, R, C, cnt
    for i in range(2):
        r, c = machine[i] + (-1 if i == 0 else 1), 0
        for j in range(4):
            dr, dc = direction[i][j]
            for _ in range(cnt[i][j]):
                A[r][c] = A[r + dr][c + dc]
                r += dr
                c += dc
        A[r][c] = 0


dd = [(-1, 0), (0, -1), (1, 0), (0, 1)]
direction = [
    [(-1, 0), (0, 1), (1, 0), (0, -1)],
    [(1, 0), (0, 1), (-1, 0), (0, -1)]
]
R, C, T = map(int, input().split())
A = []
machine = []
for i in range(R):
    A.append(list(map(int, input().split())))
    if A[i][0] == -1:
        machine.append(i)
cnt = [
    [machine[0] - 1, C - 1, machine[0], C - 2],
    [R - machine[1] - 2, C - 1, R - machine[1] - 1, C - 2]
]
for _ in range(T):
    spread()
    wind()
print(sum(sum(a) for a in A) + 2)