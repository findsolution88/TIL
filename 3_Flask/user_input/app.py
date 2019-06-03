from flask import Flask, render_template, request
from iexfinance.stocks import Stock

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search_stock')
def search_stock():
    return render_template('search_stock.html',
                           is_first_search=True)


@app.route('/search_result')
def result():
    user_input = request.args.get('keyword')
    TOKEN = 'iexcloud.io에서 받은 token 작성'

    try:
        stock = Stock(user_input, token=TOKEN) # 검색어가 없을 경우 except로 이동
        data = stock.get_quote() #올바르지 않은 company code가 아닐 경우 except로 이동
    except:
        return render_template(
            'search_stock.html',
            is_success=False,
        )

    return render_template('search_stock.html',
                           is_success=True,
                           c_name=data['companyName'],
                           l_price=data['latestPrice'],
                           )

if __name__ =='__main__':
    app.run(debug=True)