X = int(input()) - 1

a = 1
b = 1
k = 1
switch = True
i = 0
while i < X:
    if switch:
        i += 1
        b += 1
        for j in range(k):
            if i >= X:
                break
            a += 1
            b -= 1
            i += 1
    else:
        i += 1
        a += 1
        for j in range(k):
            if i >= X:
                break
            a -= 1
            b += 1
            i += 1
    k += 1
    switch = not switch

print(f'{a}/{b}')
