data = [1, 2, 3, 4, 5]


def combination(k, r, result, arr):
    if r == 0:
        print(result)
        answer.append(tuple(result))
    elif k == len(arr):
        return
    else:
        result.append(arr[k])
        combination(k + 1, r - 1, result, arr)
        result.pop()
        combination(k + 1, r, result, arr)


answer = []
combination(0, 2, [], data)
print(answer)
