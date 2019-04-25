N = int(input())
count = 12
if N < 13:
    print(N)
else :
    for i in range(13, N+1):
        s = str(i)
        d = t_d = int(s[0])-int(s[1])
        for j in range(len(s)-1):
            t_d = int(s[j])-int(s[j+1])
            if d != t_d:
                break
        if d == t_d:
            count += 1
    print(count)