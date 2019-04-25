def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


def sub(string, length):
    for i in range(len(string) - length + 1):
        temp = string[i:i + length]
        if is_palindrome(temp):
            return temp


for T in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    inputs = ['' for _ in range(N)]
    result = None
    for index in range(N):
        string = input()
        result = sub(string, M)
        if result:
            for _ in range(N - index - 1):
                input()
            break
        string = list(string)
        for i in range(N):
            inputs[i] += string[i]
    if result is None:
        for string in inputs:
            result = sub(string, M)
            if result:
                break
    print(f'#{T} {result}')
