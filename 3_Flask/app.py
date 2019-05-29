from flask import Flask, render_template
import random
import requests
import json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def lotto():
    lucky_numbers = random.sample(range(1,46),6)
    lucky_numbers.sort()
    # return f'이번주 로또 예상 번호는 {lucky_numbers}입니다.'
    return render_template('pick_lotto.html', numbers=lucky_numbers)

@app.route('/find_lotto/<int:num>')
def find_lotto(num):
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    data = requests.get(url).text
    lotto_data = json.loads(data)

    lotto_num = []
    for i in range(1,7):
        lotto_num.append(lotto_data[f'drwtNo{i}'])
    lotto_num.sort()
    return render_template('find_lotto.html', numbers=lotto_num, num=num)


@app.route('/square/<int:num>')
def square(num):
    result = num**2
    return f'{result}'

if __name__ == '__main__':
    app.run(debug=True)