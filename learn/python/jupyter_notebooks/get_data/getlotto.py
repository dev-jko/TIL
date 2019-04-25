import requests

URL = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'
result = requests.get(URL).json()
print(result)