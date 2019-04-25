nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for T in range(1, int(input()) + 1):
    input()
    inputs = list(input().split())
    temp = [0 for _ in range(10)]
    for value in inputs:
        temp[nums.index(value)] += 1
    result = ''
    for i in range(10):
        result += (nums[i] + ' ') * temp[i]
    print(f'#{T}\n{result[:-1]}')
