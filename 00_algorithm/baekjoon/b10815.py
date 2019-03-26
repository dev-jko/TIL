# https://www.acmicpc.net/problem/10815
# 숫자 카드


def binary_search(target, left, right):
    if left >= right and target != cards[left]:
        return False
    mid = (left + right) // 2
    if target == cards[mid]:
        return True
    elif target > cards[mid]:
        return binary_search(target, mid + 1, right)
    else:
        return binary_search(target, left, mid - 1)


N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
finds = list(map(int, input().split()))
result = ''
for i in finds:
    if binary_search(i, 0, N - 1):
        result += '1 '
    else:
        result += '0 '
print(result[:-1])

# N = int(input())
# cards = sorted(list(map(int, input().split())))
# cards_dict = {}
# for i in cards:
#     cards_dict[i] = True
# M = int(input())
# finds = list(map(int, input().split()))
# result = ''
# for i in finds:
#     if i in cards_dict:
#         result += '1 '
#     else:
#         result += '0 '
# print(result[:-1])
