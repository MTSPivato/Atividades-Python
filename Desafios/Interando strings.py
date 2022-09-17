#        indices
#        0123456789....................31
frase = 'Lorem Ipsum is simply dummy text'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador <= tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    print(nova_string)
    contador += 1
