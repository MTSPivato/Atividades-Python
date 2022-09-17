"""
Operadores lógicos

and, or, not
in, e not in
"""

########################################################################################################################

# # Exemplos:
#
# # Difinindo variáveis
# a = 2
# b = 2
# c = 3
#
# # No exemplo a serguir podemos ver uma aplicação com "and" que siginifica "e"
# # Ou seja, as duas comparações tem que corresponder para validar a operação.
#
# #   true   e   false
# if a == b and a != c:
#     print(bool(True))
# else:
#     print(bool(False))
#
# # No exemplo a serguir podemos ver uma aplicação com "or" que siginifica "ou"
# # Ou seja, só uma das comparações deve corresponder para validar a operação.
#
# #   true  ou  true
# if a == b or a == c:
#     print(bool(True))
# else:
#     print(bool(False))
#
# # Ao adicionar "not" na frente de uma operação, você irá solicitar o inverso da operação.
#
# #  não é true ou  true
# if not a == b or a == c:
#     print(bool(True))
# else:
#     print(bool(False))

########################################################################################################################

# # Exemplos 2:
# a = input('Insira um valor: ')
# b = 0
#
# # Nesse caso o comparador ira interpretar o "not" como um valor nulo, exemplo:
# # (se não "variável") quer dizer que se nada estiver definido na variável a operação será validada
#
# while not a:
#     print('Por favor preencha o campo "a"')
#     a = input('Insira um valor válido: ')
#     if not not a:
#         break
#
# print(f'Você insiriu: {a}')

########################################################################################################################

# # Exemplo 3:
#
# usuario = input('Insira seu usuário: ')
# senha = input('Insira sua senha: ')
#
# usuario_bd = 'matheus'
# senha_bd = '1234'
#
# while usuario != usuario_bd and senha != senha_bd:
#     print()
#     print(f'Acesso negado, ensira suas credenciais novamente!')
#     print()
#     usuario = input('Insira seu usuário: ')
#     senha = input('Insira sua senha: ')
#     if usuario == usuario_bd and senha == senha_bd:
#         break
# print()
# print(f'Você está logado, {usuario}. Seja bem-vindo!')

