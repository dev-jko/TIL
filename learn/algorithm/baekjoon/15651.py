N, M = map(int, input().split())
N += 1
pick = []


def dfs(k):
    if k == M:
        print(*pick, sep=' ')
    else:
        for i in range(1, N):
            pick.append(i)
            dfs(k + 1)
            pick.pop()


dfs(0)
