N = int(input())
count = 0
for i in range(N):
    check = False

    s = input()

    temp = s[0]
    for c in s:
        if temp != c:
            check = False
        else :
            break
        temp = c


    if check:
        count += 1
print(count)