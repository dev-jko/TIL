def bt(n, grid, k, cnt):
    if n == k:
        return cnt + 1
    for i in range(n):
        bt(n, grid, )


N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
result = bt(N, grid, 0, 0)
print(result)
