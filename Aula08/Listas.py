"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
main, max
range
"""
# texto1 = 'Valor'
#
# #         0  1  2  3  4   5      6
# lista = [1, 2, 3, 4, 5, 'Olá', 'Bom dia']
# #        -6 -5 -4 -3 -2  -1     -0
#
# string = 'AbCdE'
#
# print(lista[6][0:3])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(l1)
#
# # Neste caso, estou adicionando
# # O VALORES da outra_lista
# # dentro da lista
#
# l1.extend('a')
#
# # Neste caso, estou adicionando outra_lista
# # dentro da lista
#
# # l1.append('a')
#
# # insert insere um valor no indice determinado
# # l1.insert(2, 'a')
#
# print(l1)
#
# l1.pop()
# l1.pop()
# print(l1)

# #     0  1  2  3  4  5  6  7  8
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(l1)
# l1.insert(0, 'Olá')
# print(l1)
# del(l1[0])
# print(l1)
#
# print(max(l1))
# print(min(l1))

# l1 = list(range(0, 11, 2))
# print(l1)
#
# l2 = range(0, 11, 2)
# soma = 0
#
# valor = 0
# for valor in l2:
#     soma = soma + valor
#     print(f'{soma} + {valor} = ')

# l2 = ['String', True, 10, -10.5]
#
# for elem in l2:
#     print(f'Otipo do elemento é {type(elem)} e seu valor é: {elem}')

secreto = 'girafa'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print()
        print(f'Você perdeu, a palavra era {secreto}')
        break

    print()
    letra = input('Digite uma letra: ')

    if len(letra) > 1 or letra.isnumeric():
        print()
        print('Valor inválido, tente novamente! ')
        continue
    digitadas.append(letra)

    if letra in secreto:
        print()
        print(f'A letra "{letra}" existe na palavra secreta! ')
    else:
        print()
        print(f'A ltra "{letra}" nãao existe na palavra secreta! ')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    print()
    print(f'Ainda restam {chances} chances')
    print()
    print(secreto_temporario)

    if letra not in secreto:
        chances -= 1

    if secreto_temporario == secreto:
        print()
        print(f'Parabéns, você acertou a palavra!')
        break
