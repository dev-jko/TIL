# https://www.acmicpc.net/problem/10816
# 숫자 카드 2


def binary_search(target, left, right):
    if left >= right and target != cards[left]:
        return -1
    mid = (left + right) // 2
    if target == cards[mid]:
        return mid
    elif target > cards[mid]:
        return binary_search(target, mid + 1, right)
    else:
        return binary_search(target, left, mid - 1)


N = int(input())
cards = sorted(list(map(int, input().split())))
cnts = [0 for _ in range(20000002)]
for i in cards:
    cnts[i + 10000000] += 1
cards = sorted(list(set(cards)))
M = int(input())
finds = list(map(int, input().split()))
result = ''
for i in finds:
    idx = binary_search(i, 0, len(cards) - 1)
    if idx != -1:
        result += '{} '.format(cnts[i + 10000000])
    else:
        result += '0 '
print(result[:-1])



# N = int(input())
# cards = sorted(list(map(int, input().split())))
# cards_dict = {}
# for i in cards:
#     if i in cards_dict:
#         cards_dict[i] += 1
#     else:
#         cards_dict[i] = 1
# M = int(input())
# finds = list(map(int, input().split()))
# result = ''
# for i in finds:
#     if i in cards_dict:
#         result += '{} '.format(cards_dict[i])
#     else:
#         result += '0 '
# print(result[:-1])
