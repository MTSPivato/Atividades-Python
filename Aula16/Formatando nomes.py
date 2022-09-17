"""
Formatando valores com modificadores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)

> - Esquerdo
< - Direito
^ - Centro
"""

num1 = 120.6
num2 = 2.76
nome = 'matHEUs'
sobrenome = 'PIvatO'
result = 323
caracteres = len(nome) + 1

# print(f'{result:2^15}')
#
# print(f'{num1:a>9.3f}')

# nome_formatado = '#{0}{1}'.format(nome, sobrenome)
nome_formatado = nome.title() + ' ' + sobrenome.title()

print(nome_formatado)
