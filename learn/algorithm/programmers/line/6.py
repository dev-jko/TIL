def add_padding(c_h, result, x, y):
    if c_h != y:
        t_s = "." * x
        if align == "TOP":
            result += [t_s] * (y - c_h)
        elif align == "BOTTOM":
            result = [t_s] * (y - c_h) + result
        else:
            tt = int((y - c_h) / 2)
            result = [t_s] * tt + result + [t_s] * tt
    return result


def make1(x, y):
    t = "." * (x - 1) + "#"
    c_h = x * 2 - 1
    result = [t] * c_h
    return add_padding(c_h, result, x, y)


def make2(x, y):
    t = "#" * x
    t2 = "." * (x - 1) + "#"
    t3 = "#" + "." * (x - 1)
    c_h = x * 2 - 1
    result = [t] + [t2] * (x - 2) + [t] + [t3] * (x - 2) + [t]
    return add_padding(c_h, result, x, y)


def make3(x, y):
    t = "#" * x
    t2 = "." * (x - 1) + "#"
    c_h = x * 2 - 1
    result = [t] + [t2] * (x - 2) + [t] + [t2] * (x - 2) + [t]
    return add_padding(c_h, result, x, y)


def make4(x, y):
    t = "#" * x
    t2 = "." * (x - 1) + "#"
    t3 = "#" + "." * (x - 2) + "#"
    c_h = x * 2 - 1
    result = [t3] * (x - 1) + [t] + [t2] * (x - 1)
    return add_padding(c_h, result, x, y)


def make5(x, y):
    t = "#" * x
    t2 = "." * (x - 1) + "#"
    t3 = "#" + "." * (x - 1)
    c_h = x * 2 - 1
    result = [t] + [t3] * (x - 2) + [t] + [t2] * (x - 2) + [t]
    return add_padding(c_h, result, x, y)


def make6(x, y):
    t = "#" * x
    t2 = "#" + "." * (x - 1)
    t3 = "#" + "." * (x - 2) + "#"
    c_h = x * 2 - 1
    result = [t2] * (x - 1) + [t] + [t3] * (x - 2) + [t]
    return add_padding(c_h, result, x, y)


def make7(x, y):
    t = "#" * x
    t2 = "." * (x - 1) + "#"
    c_h = x * 2 - 1
    result = [t] + [t2] * (c_h - 1)
    return add_padding(c_h, result, x, y)


def make8(x, y):
    t = "#" * x
    t2 = "#" + "." * (x - 2) + "#"
    c_h = x * 2 - 1
    result = [t] + [t2] * (x - 2) + [t] + [t2] * (x - 2) + [t]
    return add_padding(c_h, result, x, y)


def make9(x, y):
    t = "#" * x
    t2 = "." * (x - 1) + "#"
    t3 = "#" + "." * (x - 2) + "#"
    c_h = x * 2 - 1
    result = [t] + [t3] * (x - 2) + [t] + [t2] * (x - 1)
    return add_padding(c_h, result, x, y)


def make0(x, y):
    t = "#" * x
    t2 = "#" + "." * (x - 2) + "#"
    c_h = x * 2 - 1
    result = [t] + [t2] * (c_h - 2) + [t]
    return add_padding(c_h, result, x, y)


def makeNum(x, y, num):
    if num == "1":
        return make1(x, y)
    elif num == "2":
        return make2(x, y)
    elif num == "3":
        return make3(x, y)
    elif num == "4":
        return make4(x, y)
    elif num == "5":
        return make5(x, y)
    elif num == "6":
        return make6(x, y)
    elif num == "7":
        return make7(x, y)
    elif num == "8":
        return make8(x, y)
    elif num == "9":
        return make9(x, y)
    elif num == "0":
        return make0(x, y)


N, align = input().strip().split(' ')
N = int(N)
inputs = []
height = 0
for _ in range(N):
    t = input().strip().split(' ')
    inputs.append([int(t[0]), t[1]])
    height = max(height, inputs[-1][0])
height = height * 2 - 1

result = [""] * height
for i in inputs:
    for j in i[1]:
        str_n = makeNum(i[0], height, j)
        for k in range(height):
            result[k] += " " + str_n[k]

for i in result:
    print(i[1:])
