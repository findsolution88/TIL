from flask import Flask, render_template


import lotto_package as lp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = lp.get_random_numbers()
    # return f'이번주 로또 예상 번호는 {lucky_numbers}입니다.'
    return render_template('pick_lotto.html', numbers=lucky_numbers)


@app.route('/find_lotto/<int:num>')
def find_lotto(num):
    data = lp.get_lotto_numbers(num)

    return render_template('find_lotto.html', numbers=data, num=num)


@app.route('/lotto/<int:num>')
def lotto(num):
    lucky_numbers = lp.get_random_numbers()

    real_data = lp.get_lotto_numbers(num)
    real_numbers = real_data['real']
    bonus_number = real_data['bonus']
    winning_ammount = real_data['winning']
    rank = lp.get_result(lucky_numbers, real_numbers, bonus_number)


    return render_template('lotto.html',
                           my_numbers=lucky_numbers,
                           times=num,
                           lotto_numbers=real_numbers,
                           bonus_number=bonus_number,
                           rank=rank,
                           winning=winning_ammount)


@app.route('/square/<int:num>')
def square(num):
    result = num**2
    return f'{result}'

if __name__ == '__main__':
    app.run(debug=True)