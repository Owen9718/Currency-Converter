from flask import Flask,request,render_template,session
from forex_python.converter import CurrencyRates,CurrencyCodes,RatesNotAvailableError

c = CurrencyRates()
s = CurrencyCodes()

app = Flask(__name__)

@app.route('/')
def info():
    return render_template('home.html')

@app.route('/convert', methods=["POST"])
def convert():
    conv_from = request.form['conv_from']
    conv_to = request.form['conv_to']
    amount = None
    symbol = s.get_symbol(conv_to)
    total = None
    err = None
    try:
        amount = int(request.form['amount'])
        total = round(c.convert(conv_from,conv_to,amount),2)
    except (RatesNotAvailableError, ValueError) :
        if isinstance(amount,int):
            amount = amount
        if isinstance(amount,int) == False:
            err = "Amount must be an integer"
        if s.get_symbol(conv_from) == None:
            err = f"Currency not supported {conv_from}"
        elif s.get_symbol(conv_to) == None:
            err = f"Currency not supported {conv_to}"


    return render_template('conv.html', total = total, symbol = symbol, err = err, amount = amount)