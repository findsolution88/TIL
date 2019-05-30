from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()

TOKEN = 'pk_c099e22e063e4cabbcd9f995dcf4edc5'
aapl = Stock('FB',token=TOKEN)
data = aapl.get_quote()

pp.pprint(data)
print(data['companyName'], data['latestPrice'])