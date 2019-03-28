# 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬


def quick_sort(left, right):
    if left >= right:
        return
    p = l = left
    r = right
    while l < r:
        while l < right and data[p] >= data[l]:
            l += 1
        while data[p] < data[r]:
            r -= 1
        if l < r:
            data[l], data[r] = data[r], data[l]
    data[r], data[p] = data[p], data[r]
    quick_sort(left, r - 1)
    quick_sort(r + 1, right)


for T in range(1, int(input()) + 1):
    N = int(input())
    data = list(map(int, input().split()))
    quick_sort(0, N - 1)
    print('#{} {}'.format(T, data[N // 2]))

