# swea 5176.
# [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색


def inorder(idx):
    global n
    if idx >= len(t):
        return
    inorder(idx * 2)
    t[idx] = n
    n += 1
    inorder(idx * 2 + 1)


for T in range(1, int(input()) + 1):
    N = int(input())
    t = [0 for i in range(N + 1)]
    n = 1
    inorder(1)
    print('#{} {} {}'.format(T, t[1], t[N // 2]))
