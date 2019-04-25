for T in range(1, int(input()) + 1):
    str1, str2 = input(), input()
    cnt = [0 for _ in range(len(str1))]
    for c in str2:
        index = str1.find(c)
        if index != -1:
            cnt[index] += 1
    result = 0
    for num in cnt:
        result = max(result, num)
    print(f'#{T} {result}')
