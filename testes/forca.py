secreto = input('Insira qual será palavra secreta: ')
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
        print('Parabéns, você acertou a palavra!')
        break