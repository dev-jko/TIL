N = int(input())
col = [False for _ in range(N)]
result = 0


def bt(k):
    global result
    if N == k:
        result += 1
    else:
        for i in range(N):
            check = True
            col[k] = i
            for j in range(k):
                if col[k] == col[j] or abs(col[k] - col[j]) == abs(k - j):
                    check = False
            if check:
                bt(k + 1)


bt(0)
print(result)
