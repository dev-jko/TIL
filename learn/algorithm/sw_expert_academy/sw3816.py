a = ord('a')
for TC in range(1, int(input()) + 1):
    S1, S2 = input().split()
    s1 = [0] * 26
    for s in S1:
        s1[ord(s)-a] += 1

    s2 = [0] * 26
    for i in range(len(S1)):
        s2[ord(S2[i]) - a] += 1
    result = 1 if s1 == s2 else 0

    for i in range(len(S1), len(S2)):
        s2[ord(S2[i]) - a] += 1
        s2[ord(S2[i - len(S1)]) - a] -= 1
        for j in range(26):
            if s1[j] != s2[j]:
                break
        else:
            result += 1
    print(f'#{TC} {result}')