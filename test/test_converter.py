import sys
sys.path.append('../src/')

import unittest
import json
import requests
from converter import converter as cvt

greeting = {'message': 'Number-to-Text Converter'}
error_1 = {'ERROR': 'Input not an integer: cannot resolve'}
error_2 = {'ERROR': 'Number is out of range'}

class TestClass(unittest.TestCase):

    # Tests the INPUT, with the request (needs the server running)
    def test_input(self):
        url = 'http://0.0.0.0:4000/'
        self.assertEqual(requests.get(url).json(), greeting)
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
        self.assertEqual(cvt(100000), error_2)
        self.assertEqual(cvt(-100000), error_2)
        self.assertEqual(cvt(999999999999), error_2)
        self.assertEqual(cvt(-999999999999), error_2)

    # Tests the FUNCTION converter, not the request (range: |0-99|)
    def test_decimal(self):
        self.assertEqual(cvt(0), {'extenso': 'zero'})
        self.assertEqual(cvt(19), {'extenso': 'dezenove'})
        self.assertEqual(cvt(20), {'extenso': 'vinte'})
        self.assertEqual(cvt(29), {'extenso': 'vinte e nove'})
        self.assertEqual(cvt(-9), {'extenso': 'menos nove'})
        self.assertEqual(cvt(-20), {'extenso': 'menos vinte'})
        self.assertEqual(cvt(-29), {'extenso': 'menos vinte e nove'})

    # Tests the FUNCTION converter, not the request (range: |100-999|)
    def test_centesimal(self):
        self.assertEqual(cvt(100), {'extenso': 'cem'})
        self.assertEqual(cvt(109), {'extenso': 'cento e nove'})
        self.assertEqual(cvt(120), {'extenso': 'cento e vinte'})
        self.assertEqual(cvt(129), {'extenso': 'cento e vinte e nove'})
        self.assertEqual(cvt(200), {'extenso': 'duzentos'})
        self.assertEqual(cvt(220), {'extenso': 'duzentos e vinte'})
        self.assertEqual(cvt(229), {'extenso': 'duzentos e vinte e nove'})
        self.assertEqual(cvt(-999), {'extenso': 'menos novecentos e noventa e nove'})

    # Tests the FUNCTION converter, not the request (range: |1000-9999|)
    def test_thousand(self):
        self.assertEqual(cvt(1000), {'extenso': 'mil'})
        self.assertEqual(cvt(1009), {'extenso': 'mil e nove'})
        self.assertEqual(cvt(1100), {'extenso': 'mil e cem'})
        self.assertEqual(cvt(1109), {'extenso': 'mil e cento e nove'})
        self.assertEqual(cvt(1200), {'extenso': 'mil e duzentos'})
        self.assertEqual(cvt(1229), {'extenso': 'mil e duzentos e vinte e nove'})
        self.assertEqual(cvt(2000), {'extenso': 'dois mil'})
        self.assertEqual(cvt(2009), {'extenso': 'dois mil e nove'})
        self.assertEqual(cvt(2100), {'extenso': 'dois mil e cem'})
        self.assertEqual(cvt(2129), {'extenso': 'dois mil e cento e vinte e nove'})
        self.assertEqual(cvt(-9999), {'extenso': 'menos nove mil e novecentos e noventa e nove'})

    # Tests the FUNCTION converter, not the request (range: |1000-9999|)
    def test_tenThousand(self):
        self.assertEqual(cvt(20100), {'extenso': 'vinte mil e cem'})
        self.assertEqual(cvt(20009), {'extenso': 'vinte mil e nove'})
        self.assertEqual(cvt(20029), {'extenso': 'vinte mil e vinte e nove'})
        self.assertEqual(cvt(20129), {'extenso': 'vinte mil e cento e vinte e nove'})
        self.assertEqual(cvt(20229), {'extenso': 'vinte mil e duzentos e vinte e nove'})
        self.assertEqual(cvt(22229), {'extenso': 'vinte e dois mil e duzentos e vinte e nove'})
        self.assertEqual(cvt(-99999), {'extenso': 'menos noventa e nove mil e novecentos e noventa e nove'})


if __name__ == '__main__':
    unittest.main()

