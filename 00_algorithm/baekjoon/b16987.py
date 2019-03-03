def bt(k, n):
    global result
    if k == n:
        result = max(result, is_breaked.count(True))
    else:
        if is_breaked.count(True) >= n - 1 or result == n:
            result = max(result, is_breaked.count(True))
            return
        if is_breaked[k]:
            bt(k + 1, n)
        else:
            for i in range(N):
                if is_breaked[i] or i == k:
                    continue
                temp = (data[k][0], data[i][0])
                data[k][0] -= data[i][1]
                data[i][0] -= data[k][1]
                if data[k][0] <= 0:
                    data[k][0] = 0
                    is_breaked[k] = True
                if data[i][0] <= 0:
                    data[i][0] = 0
                    is_breaked[i] = True
                bt(k + 1, n)
                data[k][0], data[i][0] = temp
                is_breaked[k] = is_breaked[i] = False


N = int(input())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))
is_breaked = [False for _ in range(N)]
result = 0
bt(0, N)
print(result)
