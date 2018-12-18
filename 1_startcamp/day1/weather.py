from darksky import forecast
multicampus = forecast('172896b7f9ee2b8e2dbe3e1475c55cb8', 37.501322, 127.039656)
print(multicampus['currently']['summary'])
print(multicampus['currently']['temperature'])

# import requests
# url = 'https://api.darksky.net/forecast/172896b7f9ee2b8e2dbe3e1475c55cb8/37.501322,127.039656'
# res = requests.get(url).json()
# print(res['currently']['summary'])


