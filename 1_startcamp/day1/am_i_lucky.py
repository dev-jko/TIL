import requests
import random

bnusNo = 0
real_numbers = []

def getReal():
    game = 837
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
    response = requests.get(url+str(game), verify=False).json()
    bnusNo = response['bnusNo']
    for i in range(1,7):
        real_numbers.append(response['drwtNo'+str(i)])
    print('당첨번호 : ', real_numbers, '+ ' + str(bnusNo))

def func():
    my_numbers = None
    my_numbers = sorted(random.sample(list(range(1,46)), 7))
    print('내 번호 : ', my_numbers)

    count = 0
    check = False
    for i in my_numbers:
        if i in real_numbers:
            count += 1
    if count == 6:
        print('1등')
        check = True
    elif (count == 5 & bnusNo in my_numbers):
        print('2등')
        check = True
    elif count == 5:
        print('3등')
        check = True
    elif count == 4:
        print('4등')
    elif count == 3:
        print('5등')
    else :
        print('꽝')
    print('맞춘 갯수 :', count)
    return check


getReal()
while(True):
    if func():
        break