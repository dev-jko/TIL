# -*- coding: utf-8 -*-

import requests
from datetime import datetime, timedelta
from time import sleep
import os


def dict_to_csv(file, data):
    result = ''
    for info in data.values():
        temp = []
        for value in info.values():
            temp.append(value)
        result += ','.join(temp) + '\n'
    file.write(result)


def request_query(URL, headers=None, **kwargs):
    request = URL + '?'
    for key, value in kwargs.items():
        request += f'&{key}={value}'
    result = requests.get(request, headers=headers).json()
    return result


def get_week_boxoffice_info(key, total_dict, date):
    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    query = {
        'key': key,
        'targetDt': date,
        'weekGb': '0'
    }
    response = request_query(
        URL, **query)['boxOfficeResult']['weeklyBoxOfficeList']
    for movie_info in response:
        result = {}
        result['movie_code'] = movie_info['movieCd']
        result['title'] = movie_info['movieNm']
        result['audience'] = movie_info['audiAcc']
        result['recorded_at'] = date
        if result['title'] not in total_dict:
            total_dict[result['title']] = result


def get_boxoffice_info(key, get_now=False):
    info_dict = {}
    if get_now:
        now = datetime.now()
    else:
        now = datetime(2019, 1, 13)  # '20190113'
    timelist = []
    for i in range(10):
        d = -7 * i
        temp = now + timedelta(days=d)
        string = temp.strftime('%Y%m%d')
        timelist.append(string)
    for date in timelist:
        get_week_boxoffice_info(key, info_dict, date)
    return info_dict


def get_movie_info(key, total_dict, movie_code):
    URL = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    query = {
        'key': key,
        'movieCd': movie_code
    }
    response = request_query(URL, **query)['movieInfoResult']
    result = {}
    result['movie_code'] = response['movieInfo']['movieCd']
    result['movie_name_ko'] = response['movieInfo']['movieNm']
    result['movie_name_en'] = response['movieInfo']['movieNmEn'].replace(
        ',', '')
    result['movie_name_og'] = response['movieInfo']['movieNmOg']
    result['prdt_year'] = response['movieInfo']['openDt']
    result['playtime'] = response['movieInfo']['showTm']
    temp = ''
    for genre in response['movieInfo']['genres']:
        temp += genre['genreNm'] + '/'
    result['genres'] = temp[:-1]
    result['directors'] = response['movieInfo']['directors'][0]['peopleNm']
    result['watch_grade_nm'] = response['movieInfo']['audits'][0]['watchGradeNm']
    i = 0
    for actor in response['movieInfo']['actors']:
        i += 1
        if i > 3:
            break
        key = 'actor' + str(i)
        result[key] = actor['peopleNm']
    total_dict[result['movie_name_ko']] = result


def get_movie_infos(key, movie_dict):
    info_dict = {}
    for value in movie_dict.values():
        get_movie_info(key, info_dict, value['movie_code'])
    return info_dict


def get_movie_naver_info(headers, total_dict, movie_name_ko, movie_code):
    URL = 'https://openapi.naver.com/v1/search/movie.json'
    query = {
        'query': movie_name_ko
    }
    response = request_query(URL, headers, **query)['items'][0]
    result = {}
    result['movie_code'] = movie_code
    result['thumb_url'] = response['image']
    result['link_url'] = response['link']
    result['user_rating'] = response['userRating']
    total_dict[result['movie_code']] = result


def get_movie_naver_infos(headers, movie_dict):
    info_dict = {}
    for movie in movie_dict.values():
        get_movie_naver_info(headers, info_dict,
                             movie['movie_name_ko'], movie['movie_code'])
        sleep(0.2)
    return info_dict


def download_image(total_dict):
    if not os.path.exists('./images'):
        os.mkdir('./images')
    for value in total_dict.values():
        image_url = value['thumb_url']
        image_file = open(f'./images/{value["movie_code"]}.jpg', 'wb+')
        response = requests.get(image_url, stream=True)
        for block in response.iter_content(1024):
            if not block:
                break
            image_file.write(block)
        image_file.close()


if __name__ == "__main__":
    KOBIS_KEY = os.getenv('KOBIS_KEY')
    NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
    NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
    
    print(f'KOBIS_KEY : {KOBIS_KEY}')
    print(f'NAVER_CLIENT_ID : {NAVER_CLIENT_ID}')
    print(f'NAVER_CLIENT_SECRET : {NAVER_CLIENT_SECRET}')

    f = open('./boxoffice.csv', 'w+', encoding='utf-8')
    f.write('movie_code,title,audience,recorded_at\n')
    temp_dict = get_boxoffice_info(KOBIS_KEY)
    dict_to_csv(f, temp_dict)
    f.close()

    f = open('./movie.csv', 'w+', encoding='utf-8')
    f.write('movie_code,movie_name_ko,movie_name_en,movie_name_og,prdt_year,playtime,genres,directors,watch_grade_nm,actor1,actor2,actor3\n')
    temp_dict = get_movie_infos(KOBIS_KEY, temp_dict)
    dict_to_csv(f, temp_dict)
    f.close()

    headers = {
        'X-Naver-Client-Id': NAVER_CLIENT_ID,
        'X-Naver-Client-Secret': NAVER_CLIENT_SECRET
    }
    f = open('./movie_naver.csv', 'w+', encoding='utf-8')
    f.write('movie_code,thumb_url,link_url,user_rating\n')
    temp_dict = get_movie_naver_infos(headers, temp_dict)
    dict_to_csv(f, temp_dict)
    f.close()

    download_image(temp_dict)
