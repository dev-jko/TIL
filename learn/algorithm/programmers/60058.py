def solution(p):
    if p == "" or check(p):
        return p
    cnt = 1 if p[0] == '(' else -1
    u, v = "", ""
    for i in range(1, len(p)):
        if p[i] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    if check(u):
        return u + solution(v)
    return '(' + solution(v) + ')' + ''.join(map(lambda x: '(' if x == ')' else ')', u[1:-1]))


def check(string):
    if string[0] != '(':
        return False
    cnt = 1
    for c in string[1:]:
        if c == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0




inputs = [
    "(()())()",  # "(()())()"
    ")(",  # "()"
    "()))((()"  # "()(())()"
]

for i in inputs:
    print(solution(i))
