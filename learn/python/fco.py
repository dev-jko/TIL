def my_func():
    print('my_func')


def my_func2(f):
    return f


a = my_func
b = my_func2(a)
b()


def my_func3(arg):
    return arg


def arg_func():
    print('print func')


my_func3(arg_func)()


def fco():
    return lambda n: n + 1


num_100 = 100
num_101 = fco()(num_100)
print(num_101)
