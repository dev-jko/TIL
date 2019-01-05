alphabet = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
input_string = input()
for a in alphabet:
    input_string = input_string.replace(a, '1')
print(len(input_string))


# count = 0
# while len(input_string) > 0:
#     for c in alphabet:
#         if c in input_string[:len(c)]:
#             input_string = input_string[len(c):]
#             break
#     else:
#         input_string = input_string[1:]
#     count += 1
# print(count)
