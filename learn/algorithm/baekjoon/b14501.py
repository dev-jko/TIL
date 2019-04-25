#  https://www.acmicpc.net/problem/14501
# 퇴사


def bt(k, r, p, n):
    global result
    if k == n:
        temp = 0
        for i in range(1, n):
            if check[i]:
                temp += data[i][1]
        result = max(result, temp)
    else:
        if r == 0:
            if k + data[k][0] <= n:
                check[k] = True
                bt(k + 1, data[k][0] - 1, p + data[k][1], n)
            check[k] = False
            bt(k + 1, 0, p + data[k][1], n)
        else:
            bt(k + 1, r - 1, p, n)


N = int(input())
data = [0]
for _ in range(N):
    data.append(list(map(int, input().split())))
check = [False for _ in range(N + 1)]
result = 0
bt(1, 0, 0, N + 1)
print(result)
