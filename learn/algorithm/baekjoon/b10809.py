S = str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
result = ''
for c in alphabet:
    result += str(S.find(c)) + ' '
print(result)