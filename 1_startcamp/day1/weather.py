from darksky import forecast
import requests
from bs4 import BeautifulSoup


def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit-32)/1.8, 1)

multicampus = forecast('172896b7f9ee2b8e2dbe3e1475c55cb8', 37.501322, 127.039656)
print(multicampus['currently']['summary'])
print(fahrenheit_to_celsius(multicampus['currently']['temperature']))

# import requests
# url = 'https://api.darksky.net/forecast/172896b7f9ee2b8e2dbe3e1475c55cb8/37.501322,127.039656'
# res = requests.get(url).json()
# print(res['currently']['summary'])


url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text

# 얘가 중요한 것!
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

# 그래서 지금 공기가 어느정도로 안좋은건데..?
if dust > 150:
  print('매우 나쁨')
elif dust > 80:
  print('나쁨')
elif dust > 30:
  print('보통')
else:
  print('좋음')
