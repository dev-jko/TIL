T = int(input())
for i in range(T):
    s = input()
    t = 0
    score = 0
    for c in s:
        if c == 'O':
            t += 1
            score += t
        else :
            t = 0
    print(score)