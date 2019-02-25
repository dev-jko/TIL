for T in range(1, int(input()) + 1):
    string = list(input())
    length = len(string)
    while True:
        temp = length
        for i in range(len(string) - 1):
            if string[i] == string[i + 1]:
                string.pop(i)
                string.pop(i)
                temp = len(string)
                break
        if length == temp:
            break
        length = temp
    print(f'#{T} {len(string)}')
