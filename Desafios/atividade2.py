# Atividade 01:

# num = input('Insira um número: ')
#
# try:
#     resu = (int(num) % 2)
#
#     if resu == 0:
#         print(f'O número {num} é par!')
#     else:
#         print(f'O número {num} é ímpar')
#
# except:
#     print('Valor inválido, tente novamente!')

########################################################################################################################

# Atividade 02:

# horas = input('Que horsa são? ')
#
# if float(horas) <= 11:
#     print('Bom dia')
# elif float(horas) <= 17:
#     print('Boa tarde')
# elif float(horas) <= 23.59:
#     print('Boa noite')
# else:
#     print('Horário iválido')

########################################################################################################################

# Atividade 03:

# nome = input('Insira seu nome: ')
# caracteres = len(nome)
#
# while nome == '':
#     print()
#     print('Nome inválido, tente novamente!')
#     print()
#     nome = input('Insira seu nome: ')
#     caracteres = len(nome)
#     if caracteres > 0:
#         if caracteres <= 4:
#             print()
#             print(f'{nome}, seu nome é curto, ele possi {caracteres} caracteres.')
#         elif caracteres <= 6:
#             print()
#             print(f'{nome}, seu nome tem um tamanho normal, ele possi {caracteres} caracteres.')
#         else:
#             print()
#             print(f'{nome}, seu nome é longo, ele possi {caracteres} caracteres.')
#             break
