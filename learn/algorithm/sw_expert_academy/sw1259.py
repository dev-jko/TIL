for T in range(1, int(input()) + 1):
    n = int(input())
    temp = list(map(int, input().split()))
    arr = [
        [temp[num], temp[num + 1]] for num in range(0, n * 2, 2)
    ]
    check = len(arr)
    while len(arr) > 1:
        for i in range(len(arr) - 1):
            if arr[i][-1] == arr[i + 1][0]:
                arr[i] += arr[i + 1]
                arr.remove(arr[i + 1])
                break
            elif arr[i][0] == arr[i + 1][-1]:
                arr[i + 1] += arr[i]
                arr.remove(arr[i])
                break
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            if check == len(arr):
                break
            check = len(arr)
    result = ' '.join(map(str, arr[0]))
    print(f'#{T} {result}')
