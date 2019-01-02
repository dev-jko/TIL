import requests

game = 837
url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
response = requests.get(url+str(game), verify=False).json()


real_numbers = []
for i in range(1,7):
    real_numbers.append(response['drwtNo'+str(i)])
print(real_numbers, '+ ' + str(response['bnusNo']))


real_numbers2 = []
for key in response:
    if key[:-1] == 'drwtNo':
        real_numbers2.append(response[key])
print(real_numbers2)
for key in response:
    if 'drwtNo' in key:
        real_numbers2.append(response[key])
print(real_numbers2)


real_numbers3 = []
for key, value in response.items():
    if 'drwtNo' in key:
        real_numbers3.append(value)
print(real_numbers3)

