N, M = map(int, input().split())
N += 1
pick = []


def dfs(k, r):
    if r == M:
        print(*pick, sep=' ')
    elif k == N:
        return
    else:
        pick.append(k)
        dfs(k + 1, r + 1)
        pick.pop()
        dfs(k + 1, r)


dfs(1, 0)
