# 3234. 준환이의 양팔저울

# TODO   못 풀었음

def dfs(k, rw, lw):
    if k == N:
        global cnt
        cnt += 1
    else:
        if lw < (MIN * k) >> 1 or rw > (MAX * k) >> 1:
            return
        for i in range(N):
            if not used[i]:
                used[i] = True
                dfs(k + 1, rw, lw + data[i])
                if lw >= rw + data[i]:
                    dfs(k + 1, rw + data[i], lw)
                used[i] = False


for T in range(1, int(input()) + 1):
    N = int(input())
    data = sorted(list(map(int, input().split())), reverse=True)
    MIN = data[-1]
    MAX = data[0]
    used = [False] * N
    cnt = 0
    dfs(0, 0, 0)
    print('#{} {}'.format(T, cnt))
