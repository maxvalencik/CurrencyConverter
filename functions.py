from forex_python.converter import CurrencyRates, CurrencyCodes

# Tuple of currencies available in the API
currencies = ('eur', 'usd', 'gbp', 'cad', 'idr', 'bgn', 'ils', 'dkk',  'jpy', 'huf', 'ron', 'myr', 'sek', 'sgd', 'hkd', 'aud',
              'chf', 'krw', 'cny', 'try', 'hrk', 'nzd', 'thb', 'nok', 'rub', 'nr', 'mxn', 'zk', 'brl', 'pln', 'php', 'ar')


class Currency:
    """Class to define currency instances"""

    def __init__(self, abbrev):
        """initialize the currency"""
        self.abbreviation = abbrev

    def check(self):
        """check the validity of the currency"""
        if self.abbreviation in currencies:
            return True
        else:
            return False


def convertion(amount, from_curr, to_curr):
    """Function that converts an amount between two cuurencies using the forex_API"""

    # API Request
    c = CurrencyRates()
    # Error handling for request to API
    try:
        value = float(amount)
        result = c.convert(
            from_curr.abbreviation, to_curr.abbreviation, value)
    except ValueError:
        return False
    except:
        return 'API_error'

    # Test for validity of currencies entered as parameters
    if not (from_curr.abbreviation in currencies and to_curr.abbreviation in currencies):
        return

    return result


def symbol(curr):
    """Function to return symbol associated with currency from the API"""

    # API request with error handling
    s = CurrencyCodes()
    try:
        symbol = s.get_symbol(curr.abbreviation.upper())
    except ValueError:
        return False

    return symbol
