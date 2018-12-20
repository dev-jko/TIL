import requests
import random

def get_real_lotto(game_number):
    real_numbers = {'numbers':[], 'bonus':0}
    game_number = 837
    url = 'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo='
    response = requests.get(url+str(game_number), verify=False).json()
    real_numbers['bonus'] = response['bnusNo']
    for i in range(1,7):
        real_numbers['numbers'].append(response['drwtNo'+str(i)])
    print('당첨번호 : ', real_numbers['numbers'], '+ ' + str(real_numbers['bonus']))
    return real_numbers

def pick_lotto():
    return sorted(random.sample(list(range(1,46)), 7))

def am_i_lucky(my_numbers, real_numbers):
    print('내 번호 : ', my_numbers)
    count = 0
    check = False
    for i in my_numbers:
        if i in real_numbers['numbers']:
            count += 1
    if count == 6:
        print('1등')
        check = True
    elif (count == 5 & real_numbers['bonus'] in my_numbers):
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


game_number = int(input('회차 입력 : '))
real_numbers = get_real_lotto(game_number)
count = 0
while(True):
    my_numbers = pick_lotto()
    count += 1
    if am_i_lucky(my_numbers, real_numbers):
        break
print(count)