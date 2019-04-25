for T in range(1, int(input()) + 1):
    input()
    nums = list(map(int, input().split()))
    nums.sort()
    result = ' '.join(map(str, nums))
    print(f'#{T} {result}')
