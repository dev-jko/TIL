def check(s):
    stack = []
    r = []

    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                r.append(i)
    print(stack)
    print(r)


for TC in range(1, int(input()) + 1):
    L = int(input())
    S = input()
    if len(S) % 2:
        print(f"#{TC} {-1}")
        continue
    print(check(S))





# 2
# 2
# )(
# 10
# )))))(((((