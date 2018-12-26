from bs4 import BeautifulSoup
import requests

def get_rank_list():
    url = 'https://datalab.naver.com/keyword/realtimeList.naver'
    response = requests.get(url).text
    print(response)
    soup = BeautifulSoup(response, 'html.parser')
    data_set = soup.select('.title')
    print(data_set)


if __name__ == '__main__':
    get_rank_list()


# import requests
# url = 'https://api.darksky.net/forecast/172896b7f9ee2b8e2dbe3e1475c55cb8/37.501322,127.039656'
# res = requests.get(url).json()
# print(res['currently']['summary'])

