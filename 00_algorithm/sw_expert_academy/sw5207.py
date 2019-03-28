# 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색


def binary_search(target, left, right, direction):
    if left > right:
        return
    mid = (left + right) // 2
    if a[mid] == target:
        global result
        result += 1
    elif a[mid] > target and direction != 0:
        binary_search(target, left, mid - 1, 0)
    elif a[mid] < target and direction != 1:
        binary_search(target, mid + 1, right, 1)


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    result = 0
    for i in range(M):
        binary_search(b[i], 0, N - 1, None)
    print('#{} {}'.format(T, result))
