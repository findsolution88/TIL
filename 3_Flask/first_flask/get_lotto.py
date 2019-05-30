import requests
import json

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=859'
data = requests.get(url).text
lotto_data = json.loads(data)

lotto_num = []
for i in range(6) :
    lotto_num.append(lotto_data[f'drwtNo{i+1}'])

lotto_num
# print(lotto_num)
# print(lotto_data['firstWinamnt'])
#print(lotto_data)