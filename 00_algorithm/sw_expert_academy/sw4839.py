import my_std


def binary_search(arr, key):
    cnt = 0
    start = 0
    end = len(arr) - 1
    while start < end:
        cnt += 1
        mid = (start + end) >> 1
        if key == arr[mid]:
            return cnt
        elif key > arr[mid]:
            start = mid
        else:
            end = mid
    return -1


for T in range(1, int(input()) + 1):
    P, A, B = map(int, input().split())
    arr = [x for x in range(1, P + 1)]
    a = binary_search(arr, A)
    b = binary_search(arr, B)
    result = 0
    if a < b:
        result = 'A'
    elif a > b:
        result = 'B'
    print(f'#{T} {result}')
