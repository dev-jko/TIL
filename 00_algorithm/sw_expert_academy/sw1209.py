for _ in range(1, 11):
    T = input()
    sums = [
        [0 for _ in range(100)],
        [0, 0]
    ]
    Max = 0
    for i in range(100):
        temp = list(map(int, input().split()))
        Sum = 0
        for num in temp:
            Sum += num
        Max = max(Max, Sum)
        for j in range(100):
            sums[0][j] += temp[j]
        sums[1][0] += temp[i]
        sums[1][1] += temp[100 - i - 1]
    for i in sums[0]:
        Max = max(Max, i)
    Max = max(Max, sums[1][0], sums[1][1])
    print(f'#{T} {Max}')
