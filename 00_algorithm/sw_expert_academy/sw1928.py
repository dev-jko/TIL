for T in range(1, int(input()) + 1):
    string = input()
    decode = ''
    result = ''
    for c in string:
        ord_c = ord(c)
        if ord('A') <= ord_c <= ord('Z'):
            temp = str(bin(ord_c - ord('A')))[2:]
        elif ord('a') <= ord_c <= ord('z'):
            temp = str(bin(ord_c - ord('a') + 26))[2:]
        elif ord('0') <= ord_c <= ord('9'):
            temp = str(bin(ord_c - ord('0') + 52))[2:]
        elif c == '+':
            temp = str(bin(62))[2:]
        else:
            temp = str(bin(63))[2:]
        decode += temp if len(temp) >= 6 else '0' * (6 - len(temp)) + temp

    for i in range(8, len(decode), 8):
        temp = decode[i - 8:i]
        result += chr(int(temp, 2))
    print(f'#{T} {result}.')
