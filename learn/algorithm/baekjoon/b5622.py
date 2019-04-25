word = input()
count = 0
for c in word:
    if c in 'ABC':
        count += 3
    elif c in 'DEF':
        count += 4
    elif c in 'GHI':
        count += 5
    elif c in 'JKL':
        count += 6
    elif c in 'MNO':
        count += 7
    elif c in 'PQRS':
        count += 8
    elif c in 'TUV':
        count += 9
    elif c in 'WXYZ':
        count += 10
print(count)
