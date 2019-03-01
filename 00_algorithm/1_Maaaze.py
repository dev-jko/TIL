from collections import deque

dxyz = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]


def dfs(n, k):
    if k == n:
        global d
        if miro[floor[0]][state[floor[0]]][0][0] == 0 or miro[floor[4]][state[floor[4]]][4][4] == 0:
            return
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    d[i][j][k] = -1

        # bfs 실행
        q = deque()
        q.append((0, 0, 0))
        d[0][0][0] = 0
        while len(q):
            v = q.popleft()
            x, y, z = v[0], v[1], v[2]
            for value in dxyz:
                nx, ny, nz = x + value[0], y + value[1], z + value[2]
                if 0 <= nx < 5 and 0 <= ny < 5 and 0 <= nz < 5:
                    if d[nz][nx][ny] == -1 and miro[floor[nz]][state[floor[nz]]][nx][ny] == 1:
                        d[nz][nx][ny] = d[z][x][y] + 1
                        q.append((nx, ny, nz))
        global result
        if d[4][4][4] == -1:
            return
        elif d[4][4][4] < result or result == -1:
            result = d[4][4][4]
    else:
        if result == 12: return
        for i in range(4):
            state[k] = i
            for j in range(5):
                if floor[j] == -1:
                    floor[j] = k
                    dfs(n, k + 1)
                    floor[j] = -1


miro = []
for _ in range(5):
    temp = [[], [], [], []]
    for i in range(5):
        temp[0].append(list(map(int, input().split())))
    miro.append(temp)

# miro 층, 상태, i, j
# floor 층별 판 인덱스

for k in range(5):
    miro[k][1] = [[0 for _ in range(5)] for _ in range(5)]
    miro[k][2] = [[0 for _ in range(5)] for _ in range(5)]
    miro[k][3] = [[0 for _ in range(5)] for _ in range(5)]
    for l in range(1, 4):
        for i in range(5):
            for j in range(5):
                miro[k][l][j][4 - i] = miro[k][l - 1][i][j]

d = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(5)]
state = [0 for _ in range(5)]
floor = [-1 for _ in range(5)]
result = -1
dfs(5, 0)
print(result)
