answer = [i for i in range(1, 10)]
for t in range(1, int(input()) + 1):
    arrs1 = []
    arrs2 = [[0] * 9 for _ in range(9)]
    check = True
    for i in range(9):
        temp = list(map(int, input().split()))
        arrs1.append(temp)
        for j in range(9):
            arrs2[j][i] = temp[j]
    for arr in arrs1:
        temp = sorted(arr)
        if temp != answer:
            check = False
            break
    else:
        for arr in arrs2:
            temp = sorted(arr)
            if temp != answer:
                check = False
                break
        else:
            arr1 = []
            arr2 = []
            arr3 = []
            count = 0
            for arr in arrs1:
                count += 1
                arr1 += arr[:3]
                arr2 += arr[3:6]
                arr3 += arr[6:]
                if count == 3:
                    if sorted(arr1) != answer or sorted(arr2) != answer or sorted(arr3) != answer:
                        check = False
                        break
                    count = 0
                    arr1 = []
                    arr2 = []
                    arr3 = []

    print(f'#{t} {1 if check else 0}')
