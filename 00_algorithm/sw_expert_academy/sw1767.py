dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bt(k, n, sum_line):
    global result, data, cores, core_lines, states
    if k == n:
        if n - states.count(0) > result[0]:
            result[0], result[1] = n - states.count(0), len(sum_line)
        elif n - states.count(0) == result[0] and result[1] > len(sum_line):
            result[1] = len(sum_line)
    else:
        for i in range(len(core_lines[k])):
            states[k] = i
            if len(core_lines[k][i] & sum_line) != 0 or n - states[:k + 1].count(0) < result[0]:
                continue
            sum_line = sum_line.union(core_lines[k][i])
            bt(k + 1, n, sum_line)
            sum_line = sum_line.difference(core_lines[k][i])


for T in range(1, int(input()) + 1):
    N = int(input())
    data = []
    for _ in range(N):
        data.append(list(map(int, input().split())))
    cores = []
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                cores.append((i, j))
    core_lines = []
    connected = []
    for i in range(len(cores)):
        core = cores[i]
        core_lines.append([])
        if core[0] in [0, N - 1] or core[1] in [0, N - 1]:
            connected.append(core)
            continue
        core_lines[i].append(set({}))
        for d in dxy:
            nx, ny = core[0] + d[0], core[1] + d[1]
            temp = set({})
            while 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 0:
                temp.add((nx, ny))
                nx += d[0]
                ny += d[1]
            if 0 <= nx < N and 0 <= ny < N and data[nx][ny] == 1:
                continue
            if not 0 <= nx < N or not 0 <= ny < N or data[nx - d[0]][ny - d[1]] == 0:
                core_lines[i].append(temp)
    for core in connected:
        cores.remove(core)
        core_lines.remove([])
    result = [1, 999999]
    states = [0 for _ in range(len(cores))]
    bt(0, len(cores), set({}))
    print(f'#{T} {result[1]}')
