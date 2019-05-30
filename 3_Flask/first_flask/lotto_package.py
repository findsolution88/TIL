import random
import requests
import json

def get_lotto_numbers(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    data = requests.get(url).text  # type = string
    lotto_data = json.loads(data)  # type = dict
    bonus_no = lotto_data['bnusNo']
    winning = lotto_data['firstAccumamnt']

    lotto_num = []
    if lotto_data['returnValue'] == 'success':
        for i in range(1, 7):
            lotto_num.append(lotto_data[f'drwtNo{i}'])
        lotto_num.sort()

    return {'real' : lotto_num, 'bonus':bonus_no, 'winning':winning}

def get_random_numbers():
    numbers = random.sample(range(1,46),6)
    return sorted(numbers)

def get_result(real_list, random_list, bonus):
    lucky = set(real_list)
    real = set(random_list)

    match_count = len(real.intersection(lucky))

    rank ='꽝'
    if match_count == 6 :
        rank = '1등'
    elif match_count ==5 and bonus in real_list:
        rank = '2등'
    elif match_count ==5 :
        rank = '3등'
    elif match_count == 4:
        rank = '4등'
    elif match_count == 3:
        rank = '5등'

    return rank

print(__name__)
