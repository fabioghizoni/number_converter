# Number text parts, the index of the arrays correspond to the texts
n_text = {
    'uni': ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
            'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze',
            'dezesseis', 'dezessete', 'dezoito', 'dezenove'],
    'dec': ['', '', 'vinte', 'trinta', 'quarenta', 'cinquenta',
            'sessenta', 'setenta', 'oitenta', 'noventa'],
    'cent': ['', 'cento', 'duzentos', 'trezentos', 'quatrocentos',
            'quinhentos', 'seicentos', 'setecentos', 'oitocentos', 'novecentos'],
    'spec': ['cem', 'mil'] # Special
}

def converter(num):
    # Selects where the number is in range
    if abs(num) < 100:
        text = dec_converter(abs(num))
    elif abs(num) < 1000:
        text = cent_converter(abs(num))
    elif abs(num) < 100000:
        text = high_converter(abs(num))
    else:
        return { 'ERROR': 'Number is out of range' }

    # Deals with negative numbers
    if num < 0:
        text = 'menos ' + text

    return { 'extenso': text }

def dec_converter(num):
    # Here it follows the list, very straight forward
    if num < 20:
        return n_text['uni'][num]

    # Here it splits the number and builds the text accordingly
    n_array = list(str(num))
    text = n_text['dec'][int(n_array[0])]
    if n_array[1] != '0':
        text = text + ' e ' + n_text['uni'][int(n_array[1])]

    return text

def cent_converter(num):
    # Deals with a sole exception when it is '100'
    if num == 100:
        return 'cem'

    # Splits the number, builds centesimal and adds the decimal part with dec_converter
    n_array = list(str(num))
    n_dec = int(''.join(n_array[-2:]))

    text = n_text['cent'][int(n_array[0])]
    if n_dec != 0:
        text = text + ' e ' + dec_converter(n_dec)

    return text

def high_converter(num):
    return ''
