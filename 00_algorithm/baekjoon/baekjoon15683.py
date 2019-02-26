import copy

d = [0,
     [[[-1, 0]], [[0, 1]], [[1, 0]], [[0, -1]]],
     [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
     [[[-1, 0], [0, 1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]], [[-1, 0], [0, -1]]],
     [[], [], [], []],
     [[[-1, 0], [0, 1], [1, 0], [0, -1]]]
     ]


def setbound():
    global data, N, M, cctv
    data_copy = copy.deepcopy(data)
    for tv in cctv:
        # 0 위, 1 오른쪽, 2 아래, 3 왼쪽
        # data_copy[tv[0]][tv[1]]
        # for xxxx in d[]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if data_copy[i][j] == 0:
                cnt += 1
    return cnt


def dfs(k, n):
    global result, cctv
    if k == n:
        result = min(result, setbound())
    else:
        for i in range(4):
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
        if data[i][j] == [1, 2, 3, 4, 5]:
            cctv.append([i, j, 0])
dfs(0, len(cctv))
print(result)
