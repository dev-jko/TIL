import sys

sys.setrecursionlimit(10 ** 6)

pre_result = []
post_result = []


def pre_order(arr):
    if len(arr) == 0:
        return
    pre_result.append(arr[0][2])
    left = list(filter(lambda x: x[0] < arr[0][0], arr))
    right = list(filter(lambda x: x[0] > arr[0][0], arr))
    pre_order(left)
    pre_order(right)


def post_order(arr):
    if len(arr) == 0:
        return
    new_arr_left = list(filter(lambda x: x[0] < arr[0][0], arr))
    new_arr_right = list(filter(lambda x: x[0] > arr[0][0], arr))
    post_order(new_arr_left)
    post_order(new_arr_right)
    post_result.append(arr[0][2])


def solution(nodeinfo):
    new_nodeinfo = [[nodeinfo[i][0]] + [nodeinfo[i][1] * -1] + [i + 1] for i in range(len(nodeinfo))]
    new_nodeinfo2 = sorted(new_nodeinfo, key=lambda x: (x[1], x[0]))
    pre_order(new_nodeinfo2)
    post_order(new_nodeinfo2)
    return [pre_result, post_result]
