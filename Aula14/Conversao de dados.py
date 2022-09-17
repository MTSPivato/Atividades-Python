"""
ALguns tipos de conversão de dados e seus filtros

Algumas funções de conversão ("isnumeric" "isdigit" "isdecimal")
"""

# import re
#
#
# def is_float(val):
#     if isinstance(val, float): return True
#     if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_int(val):
#     if isinstance(val, int): return True
#     if re.search(r'^\-{,1}[0-9]+$', val): return True
#
#     return False
#
#
# def is_number(val):
#     return is_int(val) or is_float(val)
#
#
# num1 = input('Insira o primeiro número: ')
# num2 = input('Insira o segundo número: ')
#
# if is_number(num1) and is_number(num2):
#     num1 = float(num1)
#     num2 = float(num2)
#     print(num1 + num2)
# else:
#     print('Erro de validação')

num1 = input('Insira o primeiro número: ')
num2 = input('Insira o segundo número: ')

try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1 + num2)
except:
    print('Erro de validação')
