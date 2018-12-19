nums = list(map(int, input().split()))
if nums == [1,2,3,4,5,6,7,8]:
    print('ascending')
elif nums == [8,7,6,5,4,3,2,1]:
    print('descending')
else :
    print('mixed')


# result = 'mixed'
# if nums[0] == 1:
#     for i in range(1, 9):
#         if i != nums[i-1]:
#             break
#         if i == 8 :
#             result = 'ascending'
# elif nums[0] == 8:
#     nums = nums[::-1]
#     for i in range(1, 9):
#         if i != nums[i-1]:
#             break
#         if i == 8 :
#             result = 'descending'
# print(result)