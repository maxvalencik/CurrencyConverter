from unittest import TestCase

from requests import sessions
from app import app
from flask import session, config, json
from functions import Currency, convertion, symbol, currencies


class AppTests(TestCase):

    def setUp(self):
        """To do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_welcome(self):
        """Make sure the instruction page displays properly"""

        with self.client:
            res = self.client.get('/')
            self.assertEqual(res.status_code, 200, res.data)
            self.assertIn(b'<p class="error">', res.data)

    def test_show_forex(self):
        """Make sure the forex page shows properly"""

        with self.client:
            with self.client.session_transaction() as session:
                session['result'] = ''
        res = self.client.get('/forex')

        self.assertEqual(res.status_code, 200, res.data)
        self.assertNotIn(
            b'<div class="alert alert-success" role="alert">', res.data)
        self.assertIn(b'<option value="usd">usd</option>', res.data)

        with self.client.session_transaction() as session:
            session['result'] = '40 = 40'
        res = self.client.get('/forex')

        self.assertIn(
            b'<div class="alert alert-success" role="alert">40 = 40</div>', res.data)

    def test_convert(self):
        """Make sure convertion is handled properly in the app"""

        # Test convertion andd symbol functions
        from_curr = Currency('usd')
        to_curr = Currency('usd')
        result_expect = convertion(1, from_curr, to_curr)
        symb_from_expect = symbol(from_curr)
        symb_to_expect = symbol(to_curr)\

        self.assertEqual(result_expect, 1.0)
        self.assertEqual(symb_from_expect, 'US$')
        self.assertEqual(symb_to_expect, 'US$')

        # Test the redirection
        with self.client:
            # test validity of result
            res = self.client.get(
                '/convert?convert_from=usd&convert_to=usd&value=1')

        self.assertEqual(res.status_code, 302, res.data)

        # test flash message
        expected_flash_message = '- is not a valid currency to convert from...'
        res = self.client.get('/convert?convert_from=-&convert_to=usd&value=1')

        with self.client.session_transaction() as session:
            # returns list of flash messages
            flash_message = session['_flashes']

        self.assertEqual(res.status_code, 302, res.data)
        self.assertIn(expected_flash_message, flash_message[1][1])
