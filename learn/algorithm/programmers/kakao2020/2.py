def my_func(w):
    if w == "":
        return w

    for i in range(2, len(w) + 1, 2):
        u = w[:i]
        v = w[i:]
        if u.count("(") != u.count(")"):
            continue
        if is_correct(u):
            v = my_func(v)
            return u + v
        else:
            t = "(" + my_func(v) + ")"
            tt = ""
            for j in u[1:-1]:
                if j == "(":
                    tt += ")"
                else:
                    tt += "("
            return t + tt


def is_correct(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append("(")
        else:
            if len(stack) == 0 or stack.pop() != "(":
                return False
    return len(stack) == 0


def solution(p):
    answer = my_func(p)
    return answer


inputs = "(()())()"

# print(is_correct("()"))
# print(is_correct("())("))

print(solution(inputs))
