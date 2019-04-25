'''
12 33 44 555 666 7777 8888 99999
'''


def get_count(x, y):
    index = 0
    d = (y - x) / 2
    num = 0
    for i in range(0, y - x + 1):
        num += i
        if num - i < d <= num:
            index = i
            break
    print(f'sum : {num}, i : {index}')
    avg = (num + num - index) / 2
    if d > avg:
        return index * 2
    else:
        return index * 2 - 1


result = ''
for i in range(int(input())):
    # print(get_count(map(int, input().split())))
    result += str(get_count(*map(int, input().split()))) + '\n'
print(result)


# def get_count(x, y):
#     d = y - x
#     if d < 3:
#         return d
#     now = 2
#     count = 2
#     k = 1
#     while now < d:
#         for _ in range(2):
#             count += 1
#             now += 1
#             for _ in range(k):
#                 now += 1
#                 if now >= d:
#                     return count
#             if now >= d:
#                 return count
#         k += 1
#     return count


# T = int(input())
# for i in range(T):
#     x, y = map(int, input().split())
#     d = y - x
#     s = 0
#     count = 0
#     while d > 0:
#         if d <= s + 1:
#             count += 1
#             break
#         elif d <= s * 2:
#             count += 2
#             break
#         s += 1
#         d -= s * 2
#         count += 2
#     print(count)
