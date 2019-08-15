import unittest
import requests
from converter import converter as cvt

greeting = {'message': 'Number-to-Text Converter'}
error_1 = {'ERROR': 'Input not an integer: cannot resolve'}
error_2 = {'ERROR': 'Number is out of range'}


class TestClass(unittest.TestCase):
    # Tests the INPUT, with the request (needs the server running)
    def test_input(self):
        url = 'http://0.0.0.0:4000/'
        res = {'extenso': 'dez'}
        self.assertEqual(requests.get(url + '10').json(), res)
        self.assertEqual(requests.get(url).json(), greeting)
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
        res = {'extenso': 'zero'}
        self.assertEqual(cvt(0), res)
        res = {'extenso': 'dezenove'}
        self.assertEqual(cvt(19), res)
        res = {'extenso': 'vinte'}
        self.assertEqual(cvt(20), res)
        res = {'extenso': 'vinte e nove'}
        self.assertEqual(cvt(29), res)
        res = {'extenso': 'menos nove'}
        self.assertEqual(cvt(-9), res)
        res = {'extenso': 'menos vinte'}
        self.assertEqual(cvt(-20), res)
        res = {'extenso': 'menos vinte e nove'}
        self.assertEqual(cvt(-29), res)

    # Tests the FUNCTION converter, not the request (range: |100-999|)
    def test_centesimal(self):
        res = {'extenso': 'cem'}
        self.assertEqual(cvt(100), res)
        res = {'extenso': 'cento e nove'}
        self.assertEqual(cvt(109), res)
        res = {'extenso': 'cento e vinte'}
        self.assertEqual(cvt(120), res)
        res = {'extenso': 'cento e vinte e nove'}
        self.assertEqual(cvt(129), res)
        res = {'extenso': 'duzentos'}
        self.assertEqual(cvt(200), res)
        res = {'extenso': 'duzentos e vinte'}
        self.assertEqual(cvt(220), res)
        res = {'extenso': 'duzentos e vinte e nove'}
        self.assertEqual(cvt(229), res)
        res = {'extenso': 'menos novecentos e noventa e nove'}
        self.assertEqual(cvt(-999), res)

    # Tests the FUNCTION converter, not the request (range: |1000-9999|)
    def test_thousand(self):
        res = {'extenso': 'mil'}
        self.assertEqual(cvt(1000), res)
        res = {'extenso': 'mil e nove'}
        self.assertEqual(cvt(1009), res)
        res = {'extenso': 'mil e cem'}
        self.assertEqual(cvt(1100), res)
        res = {'extenso': 'mil e cento e nove'}
        self.assertEqual(cvt(1109), res)
        res = {'extenso': 'mil e duzentos'}
        self.assertEqual(cvt(1200), res)
        res = {'extenso': 'mil e duzentos e vinte e nove'}
        self.assertEqual(cvt(1229), res)
        res = {'extenso': 'dois mil'}
        self.assertEqual(cvt(2000), res)
        res = {'extenso': 'dois mil e nove'}
        self.assertEqual(cvt(2009), res)
        res = {'extenso': 'dois mil e cem'}
        self.assertEqual(cvt(2100), res)
        res = {'extenso': 'dois mil e cento e vinte e nove'}
        self.assertEqual(cvt(2129), res)
        res = {'extenso': 'menos nove mil e novecentos e noventa e nove'}
        self.assertEqual(cvt(-9999), res)

    # Tests the FUNCTION converter, not the request (range: |10000-99999|)
    def test_tenThousand(self):
        res = {'extenso': 'vinte mil e cem'}
        self.assertEqual(cvt(20100), res)
        res = {'extenso': 'vinte mil e nove'}
        self.assertEqual(cvt(20009), res)
        res = {'extenso': 'vinte mil e vinte e nove'}
        self.assertEqual(cvt(20029), res)
        res = {'extenso': 'vinte mil e cento e vinte e nove'}
        self.assertEqual(cvt(20129), res)
        res = {'extenso': 'vinte mil e duzentos e vinte e nove'}
        self.assertEqual(cvt(20229), res)
        res = {'extenso': 'vinte e dois mil e duzentos e vinte e nove'}
        self.assertEqual(cvt(22229), res)
        res = {'extenso':
               'menos noventa e nove mil e novecentos e noventa e nove'}
        self.assertEqual(cvt(-99999), res)


if __name__ == '__main__':
    unittest.main()
