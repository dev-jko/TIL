def is_palindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True


def sub(string, big):
    for num in range(100, big, -1):
        for i in range(len(string) - num + 1):
            temp = string[i:i + num]
            if is_palindrome(temp):
                return num
    return big


for T in range(1, 11):
    input()
    inputs = ['' for _ in range(100)]
    result = 0
    for index in range(100):
        string = input()
        result = sub(string, result)
        if result == 100:
            for _ in range(100 - index - 1):
                input()
            break
        string = list(string)
        for i in range(100):
            inputs[i] += string[i]
    if result < 100:
        for string in inputs:
            result = sub(string, result)
            if result == 100:
                break
    print(f'#{T} {result}')
