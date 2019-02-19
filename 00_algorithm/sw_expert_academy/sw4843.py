import my_std


def sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


for T in range(1, int(input()) + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr = sort(arr)
    result = ''
    for i in range(5):
        result += f' {arr[-i - 1]} {arr[i]}'
    print(f'#{T}{result}')
