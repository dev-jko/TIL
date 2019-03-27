# 1486. 장훈이의 높은 선반


def dfs(k, h):
    global result
    if k == N:
        if h >= B:
            result = min(result, h)
    else:
        if h >= result:
            return
        dfs(k + 1, h + S[k])
        dfs(k + 1, h)


for T in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    result = 0xffffffff
    dfs(0, 0)
    print('#{} {}'.format(T, result - B))
