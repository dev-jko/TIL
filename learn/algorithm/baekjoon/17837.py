from collections import deque

N, K = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(N)]
# 0 흰색, 1 빨간색, 2 파란색
board = [[deque() for _ in range(N)] for _ in range(N)]
mal = []
for i in range(K):
    r, c, d = map(int, input().split())
    board[r - 1][c - 1].append(i)
    mal.append([r - 1, c - 1, d])
dd = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]


def run():
    if K < 4:
        print(K)
        print(-1)
        return
    for i in range(1, 1001):
        for j in range(K):
            r, c = mal[j][0], mal[j][1]
            nr, nc = r + dd[mal[j][2]][0], c + dd[mal[j][2]][1]
            c1, c2 = 0 <= nr < N, 0 <= nc < N

            if c1 and c2:

                if pan[nr][nc] == 0:
                    t = deque()
                    tmal = board[r][c].pop()
                    while tmal != j:
                        t.appendleft(tmal)
                        tmal = board[r][c].pop()
                    t.appendleft(tmal)
                    while t:
                        tmal = t.popleft()
                        mal[tmal][0] = nr
                        mal[tmal][1] = nc
                        board[nr][nc].append(tmal)
                    if len(board[nr][nc]) >= 4:
                        print(i)
                        return
                    continue

                elif pan[nr][nc] == 1:
                    t = deque()
                    tmal = board[r][c].pop()
                    while tmal != j:
                        t.append(tmal)
                        tmal = board[r][c].pop()
                    t.append(tmal)
                    while t:
                        tmal = t.popleft()
                        mal[tmal][0] = nr
                        mal[tmal][1] = nc
                        board[nr][nc].append(tmal)
                    if len(board[nr][nc]) >= 4:
                        print(i)
                        return
                    continue

            # 벽이거나 파란색
            if mal[j][2] == 1:
                mal[j][2] = 2
            elif mal[j][2] == 2:
                mal[j][2] = 1
            elif mal[j][2] == 3:
                mal[j][2] = 4
            else:
                mal[j][2] = 3
            nr, nc = r + dd[mal[j][2]][0], c + dd[mal[j][2]][1]
            c1, c2 = 0 <= nr < N, 0 <= nc < N
            if c1 and c2:
                if pan[nr][nc] == 0:
                    t = deque()
                    tmal = board[r][c].pop()
                    while tmal != j:
                        t.appendleft(tmal)
                        tmal = board[r][c].pop()
                    t.appendleft(tmal)
                    while t:
                        tmal = t.popleft()
                        mal[tmal][0] = nr
                        mal[tmal][1] = nc
                        board[nr][nc].append(tmal)
                    if len(board[nr][nc]) >= 4:
                        print(i)
                        return

                elif pan[nr][nc] == 1:
                    t = deque()
                    tmal = board[r][c].pop()
                    while tmal != j:
                        t.append(tmal)
                        tmal = board[r][c].pop()
                    t.append(tmal)
                    while t:
                        tmal = t.popleft()
                        mal[tmal][0] = nr
                        mal[tmal][1] = nc
                        board[nr][nc].append(tmal)
                    if len(board[nr][nc]) >= 4:
                        print(i)
                        return
                    continue

                if len(board[r][c]) >= 4:
                    print(i)
                    return

    else:
        print(-1)


run()