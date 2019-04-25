for T in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        if result == 1:
            break
        for j in range(len(str1)):
            if str2[i + j] != str1[j]:
                break
        else:
            result = 1
    print(f'#{T} {result}')
