N = int(input())
count = 0
for i in range(N):
    isGroup = True
    s = input()
    check = {s[0] : True}
    temp = s[0]
    while len(s) > 0:
        if s[0] in check:
            if not check[s[0]]:
                isGroup = False
                break
        else: 
            check[temp] = False
            check[s[0]] = True
            temp = s[0]
        s = s[1:]
    if isGroup:
        count += 1
print(count)
