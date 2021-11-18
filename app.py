from flask import Flask, render_template, session, redirect, jsonify, request, flash
from flask_debugtoolbar import DebugToolbarExtension
from functions import Currency, currencies, convertion, symbol


app = Flask(__name__)
app.secret_key = "nerea"
# the toolbar is only enabled in debug mode:
app.debug = True
toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


@app.route('/')
def welcome():
    session['result'] = ''
    return render_template('welcome.html')


@app.route('/convert')
def convert():

    # Get currencies from the form and Check validity
    from_currency = Currency(request.args.get('convert_from'))
    to_currency = Currency(request.args.get('convert_to'))

    if from_currency.check() is False:
        flash(
            f'{from_currency.abbreviation} is not a valid currency to convert from...')
    if to_currency.check() is False:
        flash(f'{to_currency.abbreviation} is not a valid currency to convert to...')

    # Get amount from form and make convertion
    amount = request.args.get('amount')
    result = convertion(amount, from_currency, to_currency)
    symbol_from = symbol(from_currency)
    symbol_to = symbol(to_currency)

    if result is False:
        flash('Enter a valid amount')
    elif result == 'API_error':
        flash('Rates not available...try again later')
    else:
        session['result'] = f'{symbol_from} {float(amount)} = {symbol_to} {result}'

    return redirect('/forex')


@app.route('/forex')
def show_forex():
    """Shows the forex page with form to initiate convertion and show final results when converted"""

    currency_available = currencies
    if session['result']:
        result = session['result']
    else:
        result = False

    session['result'] = ''

    return render_template('forex.html', result=result, currencies=currency_available)
