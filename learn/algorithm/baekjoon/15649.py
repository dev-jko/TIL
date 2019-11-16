N, M = map(int, input().split())
N += 1
used = [False] * N


def dfs(k, pick):
    if k == M:
        print(*pick, sep=' ')
    else:
        for i in range(1, N):
            if used[i]:
                continue
            used[i] = True
            pick.append(i)
            dfs(k + 1, pick)
            used[i] = False
            pick.pop()


dfs(0, [])
