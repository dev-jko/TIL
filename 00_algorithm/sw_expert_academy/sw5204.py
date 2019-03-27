# 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬


def merge_sort(left, right):
    if left >= right:
        return
    if (left + right) % 2 == 0:
        mid = (left + right) // 2 - 1
    else:
        mid = (left + right) // 2
    merge_sort(left, mid)
    merge_sort(mid + 1, right)
    if data[mid] > data[right]:
        global cnt
        cnt += 1
    idx = left
    idx1 = left
    idx2 = mid + 1
    while idx1 < mid + 1 and idx2 < right + 1:
        if data[idx1] < data[idx2]:
            temp[idx] = data[idx1]
            idx1 += 1
            idx += 1
        else:
            temp[idx] = data[idx2]
            idx2 += 1
            idx += 1
    while idx1 < mid + 1:
        temp[idx] = data[idx1]
        idx1 += 1
        idx += 1
    while idx2 < right + 1:
        temp[idx] = data[idx2]
        idx2 += 1
        idx += 1
    for i in range(left, right + 1):
        data[i] = temp[i]


for T in range(1, int(input()) + 1):
    N = int(input())
    cnt = 0
    data = list(map(int, input().split()))
    temp = [0] * N
    merge_sort(0, N - 1)
    print('#{} {} {}'.format(T, data[N // 2], cnt))
