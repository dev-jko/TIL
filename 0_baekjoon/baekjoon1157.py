s = str(input()).upper()
chars = {}
for c in s:
    if c in chars.keys():
        chars[c] += 1
    else:
        chars[c] = 1

result = {'char': '', 'count': 0}
check = False
for key, value in chars.items():
    if result['count'] < value:
        result['char'] = key
        result['count'] = value
        check = False
    elif result['count'] == value:
        check = True

if check:
    print('?')
else:
    print(result['char'])
