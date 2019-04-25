def quick_sort(left, right):
    if left >= right:
        return
    i, j = left, right
    while i < j:
        while i <= right and arr[i] <= arr[left]:
            i += 1
        while arr[j] > arr[left]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[left], arr[j] = arr[j], arr[left]
    quick_sort(left, j - 1)
    quick_sort(j + 1, right)


arr = [12, 5, 3, 85, 158, 32, 1, 0, 8, 65, 1, 3, 5]
print(arr, len(arr))
quick_sort(0, len(arr) - 1)
print(arr, len(arr))
