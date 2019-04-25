for T in range(1, int(input()) + 1):
    N = int(input())
    nums = set({str(x) for x in range(10)})
    count = 0
    while True:
        count += 1
        result = N * count
        string = set(str(result))
        nums = nums - string
        if len(nums) == 0:
            break
    print(f'#{T} {result}')
