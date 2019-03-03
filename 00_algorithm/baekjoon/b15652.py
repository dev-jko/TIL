# https://www.acmicpc.net/problem/15652
# N과 M (4)


def bt(k, n):
    if k == n:
        global result
        result += ' '.join(map(str, pick)) + '\n'
    else:
        for i in arr:
            if k == 0 or pick[k - 1] <= i:
                pick[k] = i
                bt(k + 1, n)


N, M = map(int, input().split())
arr = [i for i in range(1, N + 1)]
pick = [0 for i in range(M)]
result = ''
bt(0, M)
print(result)
