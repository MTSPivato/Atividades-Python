"""
For / Else com Python
"""

variavel = input('Insira uma palavra: ')
inicial = input('Insira uma inicial: ')

for valor in variavel:
    if valor == inicial:
        print(f'A inicial é: {inicial}')
        break
    else:
        print(f'A inicial não é: {inicial}')
        break
