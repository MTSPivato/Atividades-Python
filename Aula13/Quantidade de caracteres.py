"""
Leitura de quantidade de caracteres
Utilize a função "len"

Exemplos:
"""

usuario = input('Insira seu usuário: ')
caracteres = len(usuario)

# print(usuario, caracteres, type(caracteres))

while usuario == '' or caracteres > 10:
    print('Usuário inválido, tente novamente!')
    print()
    usuario = input('Insira seu usuário: ')
    caracteres = len(usuario)
    if usuario != '':
        while caracteres > 10:
            print('Usuário muito grande, tente insirir um usuário com menos de 10 caracteres!')
            print()
            usuario = input('Insira seu usuário: ')
            caracteres = len(usuario)
            if caracteres <= 10:
                break

print(f'Usuário cadastrado com sucesso, bem-vindo {usuario}!')
