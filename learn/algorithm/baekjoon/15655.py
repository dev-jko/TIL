N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
used = [False] * N
pick = []


def dfs(k):
    if k == M:
        print(*pick)
    else:
        for i in range(N):
            if used[i] or (k != 0 and pick[-1] > nums[i]):
                continue
            used[i] = True
            pick.append(nums[i])
            dfs(k + 1)
            pick.pop()
            used[i] = False


dfs(0)
