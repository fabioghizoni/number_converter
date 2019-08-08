import sys
sys.path.append('../src/')

import unittest
import json
import requests
from converter import converter

error_1 = {'ERROR': 'Input not an integer: cannot resolve'}
error_2 = {'ERROR': 'Number is out of range'}

class TestClass(unittest.TestCase):

    # Tests the INPUT, with the request (needs the server running)
    def test_input(self):
        url = 'http://0.0.0.0:4000/'
        self.assertEqual(requests.get(url + '10').json(), {'extenso': 'dez'})
        self.assertEqual(requests.get(url + '100000').json(), error_2)
        self.assertEqual(requests.get(url + '-100000').json(), error_2)
        self.assertEqual(requests.get(url + 'aaa').json(), error_1)
        self.assertEqual(requests.get(url + '1.3').json(), error_1)
        self.assertEqual(requests.get(url + '-1.3').json(), error_1)
        self.assertEqual(requests.get(url + '1,3').json(), error_1)
        self.assertEqual(requests.get(url + '_._').json(), error_1)
        self.assertEqual(requests.get(url + 'a1').json(), error_1)
        self.assertEqual(requests.get(url + '1a').json(), error_1)

    # Tests the FUNCTION converter, in regards of RANGE of numbers
    def test_outRange(self):
        self.assertEqual(converter(100000), error_2)
        self.assertEqual(converter(-100000), error_2)
        self.assertEqual(converter(999999999999), error_2)
        self.assertEqual(converter(-999999999999), error_2)

    # Tests the FUNCTION converter, not the request (range: |0-99|)
    def test_decimal(self):
        self.assertEqual(converter(0), {'extenso': 'zero'})
        self.assertEqual(converter(19), {'extenso': 'dezenove'})
        self.assertEqual(converter(20), {'extenso': 'vinte'})
        self.assertEqual(converter(29), {'extenso': 'vinte e nove'})
        self.assertEqual(converter(-9), {'extenso': 'menos nove'})
        self.assertEqual(converter(-20), {'extenso': 'menos vinte'})
        self.assertEqual(converter(-29), {'extenso': 'menos vinte e nove'})

    # Tests the FUNCTION converter, not the request (range: |100-999|)
    def test_centesimal(self):
        self.assertEqual(converter(100), {'extenso': 'cem'})
        self.assertEqual(converter(109), {'extenso': 'cento e nove'})
        self.assertEqual(converter(120), {'extenso': 'cento e vinte'})
        self.assertEqual(converter(129), {'extenso': 'cento e vinte e nove'})
        self.assertEqual(converter(200), {'extenso': 'duzentos'})
        self.assertEqual(converter(220), {'extenso': 'duzentos e vinte'})
        self.assertEqual(converter(229), {'extenso': 'duzentos e vinte e nove'})
        self.assertEqual(converter(-999), {'extenso': 'menos novecentos e noventa e nove'})

if __name__ == '__main__':
    unittest.main()

