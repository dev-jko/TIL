N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
pick = []
used = [False] * N


def dfs(k):
    if k == M:
        print(*pick, sep=' ')
    else:
        for i in range(N):
            if used[i]:
                continue
            used[i] = True
            pick.append(nums[i])
            dfs(k + 1)
            used[i] = False
            pick.pop()


dfs(0)
