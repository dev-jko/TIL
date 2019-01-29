for T in range(1, int(input()) + 1):
    nums = (2, 3, 5, 7, 11)
    counts = [0 for _ in range(5)]
    N = int(input())
    for index, num in enumerate(nums):
        while N % num == 0:
            counts[index] += 1
            N //= num
    result = ' '.join(map(str, counts))
    print(f'#{T} {result}')
