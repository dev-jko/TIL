arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
result = 0
for i in range(len(arr)):
    height = len(arr) - 1 - i
    for j in range(i + 1, len(arr)):
        if arr[i] <= arr[j]:
            height -= 1
    if result < height:
        result = height
print(result)
