def dfs(k, arr):
    global K, used, answer
    if k == K:
        t = min(sum(a) for a in arr)
        answer = min(t, answer)
    else:
        for i in range(K):
            if used[i]:
                continue
            used[i] = True
            dfs(k + 1, turn(arr, i))
            used[i] = False


def turn(arr, n):
    global command, N, M
    r, c, s = command[n]
    r -= 1
    c -= 1
    result = [a[:] for a in arr]
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for n in range(s + 1):
        i, j = r - n, c - n
        for k in range(4):
            for _ in range(n + n):
                di, dj = i + d[k][0], j + d[k][1]
                result[di][dj] = arr[i][j]
                i, j = di, dj
    return result


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
command = [list(map(int, input().split())) for _ in range(K)]
used = [False] * K
answer = 0xffffffffffff
dfs(0, A)
print(answer)
