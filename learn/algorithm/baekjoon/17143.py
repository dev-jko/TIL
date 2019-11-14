def move():
    global R, C, board
    temp = []
    for r in range(R):
        for c in range(C):
            if board[r][c] is not None:
                shark = board[r][c]
                board[r][c] = None
                nr, nc = r, c
                ts = shark[0]
                if shark[1] in (1, 2):
                    while ts > 0:
                        if nr == 0 and shark[1] == 1:
                            shark[1] = 2
                        elif nr == R - 1 and shark[1] == 2:
                            shark[1] = 1
                        nr += dd[shark[1]][0]
                        ts -= 1
                else:
                    while ts > 0:
                        if nc == C - 1 and shark[1] == 3:
                            shark[1] = 4
                        elif nc == 0 and shark[1] == 4:
                            shark[1] = 3
                        nc += dd[shark[1]][1]
                        ts -= 1
                shark[3] = nr
                shark[4] = nc
                temp.append(shark)
    for shark in temp:
        if board[shark[3]][shark[4]] and shark[2] <= board[shark[3]][shark[4]][2]:
            continue
        board[shark[3]][shark[4]] = shark


dd = [None, (-1, 0), (1, 0), (0, 1), (0, -1)]
R, C, M = map(int, input().split())
board = [[None] * C for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    if d in (3, 4):
        s = s % ((C - 1) * 2)
    else:
        s = s % ((R - 1) * 2)
    shark = [s, d, z, r - 1, c - 1]
    board[r - 1][c - 1] = shark

answer = 0
for c in range(C):
    shark = None
    for r in range(R):
        if board[r][c] is not None:
            answer += board[r][c][2]
            board[r][c] = None
            break
    move()
print(answer)
