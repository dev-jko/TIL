d = [0,
     [[[-1, 0]], [[0, 1]], [[1, 0]], [[0, -1]]],
     [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
     [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]]],
     [[[0, -1], [-1, 0], [0, 1]], [[-1, 0], [0, 1], [1, 0]],
      [[0, -1], [1, 0], [0, 1]], [[0, -1], [-1, 0], [1, 0]]],
     [[[-1, 0], [0, 1], [1, 0], [0, -1]]]
     ]


def setbound():
    global data, N, M, cctv
    for tv in cctv:
        for a in d[data[tv[0]][tv[1]]][tv[2]]:
            x, y = tv[0], tv[1]
            while True:
                x += a[0]
                y += a[1]
                if not 0 <= x < N or not 0 <= y < M or data[x][y] == 6:
                    break
                if data[x][y] != 0:
                    continue
                data[x][y] = -1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                cnt += 1
    for tv in cctv:
        for a in d[data[tv[0]][tv[1]]][tv[2]]:
            x, y = tv[0], tv[1]
            while True:
                x += a[0]
                y += a[1]
                if not 0 <= x < N or not 0 <= y < M or data[x][y] == 6:
                    break
                if data[x][y] != -1:
                    continue
                data[x][y] = 0
    return cnt


def dfs(k, n):
    global result, cctv, data
    if k == n:
        result = min(result, setbound())
    else:
        for i in range(len(d[data[cctv[k][0]][cctv[k][1]]])):
            cctv[k][2] = i
            dfs(k + 1, n)


N, M = map(int, input().split())
result = 999999
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
cctv = []
for i in range(N):
    for j in range(M):
        if data[i][j] in [1, 2, 3, 4, 5]:
            cctv.append([i, j, 0])
dfs(0, len(cctv))
print(result)
